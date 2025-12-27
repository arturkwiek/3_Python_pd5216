"""
Program: Analiza sekwencji DNA z pliku + sekwencja użytkownika + DataFrame + wykresy
Wymagania: pandas, matplotlib
Instalacja (jeśli trzeba):
    pip install pandas matplotlib
Uruchomienie:
    python main.py
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional

import pandas as pd
import matplotlib.pyplot as plt


# =========================
#  MODELE DANYCH
# =========================

@dataclass
class SequenceRecord:
    """Pojedynczy rekord sekwencji: nazwa i sama sekwencja (DNA jako tekst)."""
    name: str
    seq: str


# =========================
#  WALIDACJA I METRYKI
# =========================

VALID_NUCS = set("ATCG")


def normalize_seq(seq: str) -> str:
    """Usuwa spacje, znaki nowej linii, zamienia na wielkie litery."""
    return "".join(seq.split()).upper()


def is_valid_dna(seq: str) -> bool:
    """Sprawdza czy sekwencja składa się wyłącznie z A/T/C/G oraz nie jest pusta."""
    if not seq:
        return False
    return set(seq).issubset(VALID_NUCS)


def gc_content(seq: str) -> float:
    """Zawartość GC w procentach."""
    if not seq:
        return 0.0
    g = seq.count("G")
    c = seq.count("C")
    return 100.0 * (g + c) / len(seq)


def at_content(seq: str) -> float:
    """Zawartość AT w procentach."""
    if not seq:
        return 0.0
    a = seq.count("A")
    t = seq.count("T")
    return 100.0 * (a + t) / len(seq)


# =========================
#  PARSOWANIE PLIKU
# =========================

def parse_fasta_one_line(line: str) -> Optional[SequenceRecord]:
    """
    Oczekiwany format linii (FASTA w jednej linii):
        >NAZWA ATCGATCG...
    Zwraca SequenceRecord albo None, jeśli linia jest pusta/komentarz.
    """
    line = line.strip()
    if not line:
        return None

    if not line.startswith(">"):
        # Jeśli ktoś dał "gołą" sekwencję bez nagłówka, też spróbujemy ją przyjąć.
        # Nadamy jej automatyczną nazwę później.
        return SequenceRecord(name="", seq=normalize_seq(line))

    # Dzielimy na 2 części: nagłówek i sekwencję
    parts = line.split(maxsplit=1)
    header = parts[0][1:]  # bez '>'
    seq = normalize_seq(parts[1]) if len(parts) > 1 else ""
    return SequenceRecord(name=header, seq=seq)


def load_sequences_from_file(filepath: str) -> List[SequenceRecord]:
    """Wczytuje sekwencje z pliku tekstowego."""
    records: List[SequenceRecord] = []

    with open(filepath, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            rec = parse_fasta_one_line(line)
            if rec is None:
                continue
            # jeśli brak nazwy (bo linia bez >), nadaj automatyczną
            if not rec.name:
                rec.name = f"SEQ_{idx}"
            records.append(rec)

    return records


def append_user_sequence_to_file(filepath: str, name: str, seq: str) -> None:
    """Dopisuje sekwencję użytkownika do pliku w formacie: >NAME SEQ."""
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"\n>{name} {seq}\n")


# =========================
#  WYMÓG: każda sekwencja w oddzielnej zmiennej
# =========================

def put_sequences_into_variables(records: List[SequenceRecord]) -> Dict[str, str]:
    """
    Tworzy zmienne globalne seq_1, seq_2, ... i wkłada do nich sekwencje.
    Zwraca też słownik nazw_zmiennych -> sekwencja.
    """
    seq_vars: Dict[str, str] = {}

    for i, rec in enumerate(records, start=1):
        var_name = f"seq_{i}"
        seq_vars[var_name] = rec.seq
        globals()[var_name] = rec.seq  # tworzymy zmienną globalną

    return seq_vars


# =========================
#  CZYSZCZENIE: duplikaty i błędne sekwencje
# =========================

def deduplicate_and_filter(records: List[SequenceRecord]) -> Tuple[List[SequenceRecord], List[SequenceRecord]]:
    """
    Usuwa:
      - sekwencje niepoprawne (z innymi znakami niż A/T/C/G lub puste)
      - duplikaty (identyczna sekwencja DNA)
    Zwraca:
      (rekordy_poprawne_bez_duplikatow, rekordy_odrzucone)
    """
    rejected: List[SequenceRecord] = []
    seen: set[str] = set()
    cleaned: List[SequenceRecord] = []

    for rec in records:
        seq = rec.seq
        if not is_valid_dna(seq):
            rejected.append(rec)
            continue
        if seq in seen:
            rejected.append(rec)
            continue
        seen.add(seq)
        cleaned.append(rec)

    return cleaned, rejected


# =========================
#  SŁOWNIK -> DataFrame
# =========================

def records_to_dict(records: List[SequenceRecord]) -> Dict[str, Dict[str, object]]:
    """
    Tworzy słownik:
      {nazwa: {"sequence": ..., "length": ..., "gc": ..., "at": ...}}
    """
    data: Dict[str, Dict[str, object]] = {}
    for rec in records:
        data[rec.name] = {
            "sequence": rec.seq,
            "length": len(rec.seq),
            "gc_percent": round(gc_content(rec.seq), 2),
            "at_percent": round(at_content(rec.seq), 2),
        }
    return data


def dict_to_dataframe(data: Dict[str, Dict[str, object]]) -> pd.DataFrame:
    """Konwersja słownika do DataFrame."""
    df = pd.DataFrame.from_dict(data, orient="index")
    df.index.name = "name"
    df = df.reset_index()
    return df


# =========================
#  WYŚWIETLANIE
# =========================

def print_sequences_summary(records: List[SequenceRecord], title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)

    for rec in records:
        seq = rec.seq
        print(f"Nazwa: {rec.name}")
        print(f"  Długość: {len(seq)}")
        print(f"  GC%: {gc_content(seq):.2f}")
        print(f"  AT%: {at_content(seq):.2f}")
        print(f"  Poprawna DNA?: {is_valid_dna(seq)}")
        print("-" * 80)


# =========================
#  WIZUALIZACJE (min 3)
# =========================

def make_plots(df: pd.DataFrame, out_dir: str = "wykresy") -> None:
    os.makedirs(out_dir, exist_ok=True)

    # 1) Histogram długości
    plt.figure()
    plt.hist(df["length"], bins=10, edgecolor="black")
    plt.title("Histogram długości sekwencji")
    plt.xlabel("Długość (nt)")
    plt.ylabel("Liczba sekwencji")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "01_hist_dlugosc.png"))
    plt.close()

    # 2) Wykres słupkowy: GC% dla wszystkich sekwencji (posortowane)
    df_sorted_gc = df.sort_values("gc_percent", ascending=False)
    plt.figure(figsize=(10, 4))
    plt.bar(df_sorted_gc["name"], df_sorted_gc["gc_percent"])
    plt.title("GC% dla sekwencji (posortowane malejąco)")
    plt.xlabel("Nazwa sekwencji")
    plt.ylabel("GC%")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "02_bar_gc.png"))
    plt.close()

    # 3) Scatter: długość vs GC%
    plt.figure()
    plt.scatter(df["length"], df["gc_percent"])
    plt.title("Zależność: długość vs GC%")
    plt.xlabel("Długość (nt)")
    plt.ylabel("GC%")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "03_scatter_len_gc.png"))
    plt.close()


# =========================
#  POBRANIE SEKWENCJI OD USERA
# =========================

def get_user_sequence() -> SequenceRecord:
    """
    Prosi użytkownika o sekwencję.
    Zwraca rekord USER_... z normalizacją (wielkie litery, bez spacji).
    """
    raw = input("\nPodaj swoją sekwencję DNA (tylko A/T/C/G): ").strip()
    seq = normalize_seq(raw)
    return SequenceRecord(name="USER_SEQUENCE", seq=seq)


# =========================
#  MAIN
# =========================

def main() -> None:
    filepath = "sekwencje.txt"

    try:
        # 1) Sprawdzenie istnienia pliku
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Nie znaleziono pliku: {filepath}")

        # 2) Wczytanie rekordów z pliku
        records = load_sequences_from_file(filepath)

        # Wymóg: minimum 30 sekwencji w pliku
        if len(records) < 30:
            print(f"UWAGA: W pliku jest tylko {len(records)} sekwencji, a miało być min. 30.")

        # 3) Każda sekwencja do oddzielnej zmiennej
        seq_vars = put_sequences_into_variables(records)
        # (możesz podejrzeć np. print(seq_1), print(seq_2) itd.)

        # 4) Pobranie sekwencji od użytkownika i dopisanie do pliku
        user_rec = get_user_sequence()
        # dopisujemy do pliku niezależnie od poprawności (wymóg: "dodaj ją do pliku")
        append_user_sequence_to_file(filepath, user_rec.name, user_rec.seq)

        # umieszczamy też user sekwencję w zmiennej
        user_sequence = user_rec.seq  # <- osobna zmienna dla usera (wymóg)
        globals()["user_sequence"] = user_sequence

        # do analizy dodajemy rekord usera do listy
        records_all = records + [user_rec]

        # 5) Wyświetlenie parametrów sekwencji (z pliku + user)
        print_sequences_summary(records_all, "Podsumowanie sekwencji (plik + user)")

        # 6) Usunięcie duplikatów i wadliwych sekwencji
        cleaned, rejected = deduplicate_and_filter(records_all)

        print("\nOdrzucone rekordy (błędne lub duplikaty):")
        for r in rejected:
            reason = []
            if not is_valid_dna(r.seq):
                reason.append("NIEPOPRAWNE ZNAKI")
            # duplikat: jeśli poprawna, ale nie znalazła się w cleaned, to zwykle duplikat
            # (tu uproszczenie)
            if is_valid_dna(r.seq):
                reason.append("DUPLIKAT (albo już był)")
            print(f"  - {r.name}: {r.seq[:40]}...  ({', '.join(reason)})")

        # 7) Słownik z sekwencjami
        seq_dict = records_to_dict(cleaned)

        # 8) Słownik -> DataFrame
        df = dict_to_dataframe(seq_dict)

        # 9) Wyświetlenie DataFrame
        print("\n" + "=" * 80)
        print("DataFrame po usunięciu duplikatów i wadliwych sekwencji:")
        print("=" * 80)
        print(df.to_string(index=False))

        # 10) Wizualizacje (min 3)
        make_plots(df)
        print("\nWykresy zapisano do katalogu: wykresy/")
        print(" - 01_hist_dlugosc.png")
        print(" - 02_bar_gc.png")
        print(" - 03_scatter_len_gc.png")

        # Dodatkowy bonus: zapis DataFrame do CSV
        df.to_csv("wynik.csv", index=False, encoding="utf-8")
        print("\nZapisano też DataFrame do pliku: wynik.csv")

    except FileNotFoundError as e:
        print("BŁĄD:", e)
    except PermissionError:
        print("BŁĄD: Brak uprawnień do odczytu/zapisu pliku.")
    except KeyboardInterrupt:
        print("\nPrzerwano przez użytkownika (CTRL+C).")
    except Exception as e:
        print("Niespodziewany błąd:", e)


if __name__ == "__main__":
    print("\nStarting DNA sequence analysis program...\n")
    main()
