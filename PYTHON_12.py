# PYTHON_12 — pliki + input() + obsługa wyjątków + własny wyjątek

class NieprawidlowaSekwencjaDNA(Exception):
    def __init__(self, sekwencja, wiadomosc="Sekwencja zawiera nieprawidłowe znaki (dozwolone: A, T, C, G)"):
        self.sekwencja = sekwencja
        self.wiadomosc = wiadomosc
        super().__init__(self.wiadomosc)


def wczytaj_sekwencje_z_pliku(nazwa_pliku):
    """Odczytuje i zwraca zawartość pliku tekstowego z sekwencjami DNA."""
    with open(nazwa_pliku, "r") as plik:
        return plik.read()


def sprawdz_sekwencje_dna(sekwencja):
    """Sprawdza czy sekwencja składa się wyłącznie z A, T, C, G. W przeciwnym razie rzuca wyjątek."""
    dozwolone = set("ATCG")
    sekwencja = sekwencja.strip().upper()

    if not sekwencja:  # pusta sekwencja też jest błędem w tym zadaniu
        raise NieprawidlowaSekwencjaDNA(sekwencja, "Podano pustą sekwencję.")

    if not set(sekwencja).issubset(dozwolone):
        raise NieprawidlowaSekwencjaDNA(sekwencja)

    return sekwencja


def zapisz_sekwencje_do_pliku(nazwa_pliku, sekwencja):
    """Nadpisuje plik (tryb 'w') i zapisuje sekwencję DNA."""
    with open(nazwa_pliku, "w") as plik:
        plik.write(sekwencja)


# --- 1) Odczyt danych z pliku i obsługa FileNotFoundError ---

plik_wejsciowy = "sekwencje.txt"

try:
    zawartosc = wczytaj_sekwencje_z_pliku(plik_wejsciowy)
    print("Odczytano zawartość pliku sekwencje.txt:\n")
    print(zawartosc)
except FileNotFoundError:
    print("Błąd: Nie znaleziono pliku 'sekwencje.txt'. Upewnij się, że istnieje w tym samym folderze co skrypt.\n")

# --- 2) Pobranie danych od użytkownika i walidacja ---

try:
    nowa = input("Podaj nową sekwencję DNA (tylko A/T/C/G): ")
    nowa_poprawna = sprawdz_sekwencje_dna(nowa)

    # --- 3) Zapis do pliku (nadpisanie, jeśli istnieje) ---
    plik_wyjsciowy = "nowa_sekwencja.txt"
    zapisz_sekwencje_do_pliku(plik_wyjsciowy, nowa_poprawna)

    print(f"\nZapisano sekwencję do pliku '{plik_wyjsciowy}': {nowa_poprawna}")

except NieprawidlowaSekwencjaDNA as e:
    print(f"\nBłąd: {e.wiadomosc}")
    print(f"Problematyczna sekwencja: {e.sekwencja}")
