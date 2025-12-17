# PYTHON_6 — praca z łańcuchami znaków na przykładzie sekwencji DNA

sekwencja_dna1 = "ATGCGTAC"
sekwencja_dna2 = "GCTATGCA"

# 1) Konkatenacja (połączenie dwóch sekwencji w jedną)
dluga_sekwencja = sekwencja_dna1 + sekwencja_dna2

# 2) String slicing (wycięcie fragmentu) — np. nukleotydy od indeksu 4 do 11 (stop jest wyłączny)
fragment = dluga_sekwencja[4:12]

# 3) Metody na stringach (minimum dwie)
liczba_atg = dluga_sekwencja.count("ATG")          # ile razy występuje motyw "ATG"
pozycja_gcta = dluga_sekwencja.find("GCTA")        # pierwsza pozycja wystąpienia "GCTA" (lub -1)
po_zamianie = dluga_sekwencja.replace("T", "U")    # przykład „RNA-izacji”: T -> U (pokazowo)

# 4) Formatowanie (f-string)
wynik = (
    f"Sekwencja 1: {sekwencja_dna1}\n"
    f"Sekwencja 2: {sekwencja_dna2}\n"
    f"Połączona:   {dluga_sekwencja}\n"
    f"\tWycięty fragment [4:12]: {fragment}\n"
    f"\tcount('ATG') = {liczba_atg}\n"
    f"\tfind('GCTA')  = {pozycja_gcta}\n"
    f"\tPo replace('T'->'U'): {po_zamianie}"
)

# 5) Znak ucieczki: \n (nowa linia) i \t (tabulator) są użyte w wyniku
print(wynik)
