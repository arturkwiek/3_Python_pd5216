# Python_13.py
import os
import datetime
import biologia

# 1) Wyświetlenie tekstu z modułu biologia
print(biologia.opis_komorki())

# 2) Utworzenie katalogu dane_bio (jeśli nie istnieje)
katalog = "dane_bio"
if not os.path.exists(katalog):
    os.mkdir(katalog)

# 3) Przygotowanie danych: zliczenie nukleotydów
sekwencja = "AGCTTAGCTAAGGCT"
licznik = biologia.licz_nukleotydy(sekwencja)

# 4) Aktualna data i czas utworzenia pliku
czas_utworzenia = datetime.datetime.now()

# 5) Zapis do pliku nukleotydy.txt (w katalogu dane_bio)
sciezka = os.path.join(katalog, "nukleotydy.txt")
with open(sciezka, "w", encoding="utf-8") as plik:
    plik.write("Sekwencja DNA: " + sekwencja + "\n")
    plik.write("Liczba nukleotydów (A/T/C/G):\n")
    plik.write(f"A: {licznik.get('A', 0)}\n")
    plik.write(f"T: {licznik.get('T', 0)}\n")
    plik.write(f"C: {licznik.get('C', 0)}\n")
    plik.write(f"G: {licznik.get('G', 0)}\n")
    plik.write("\nData i czas utworzenia pliku: " + str(czas_utworzenia) + "\n")

print(f"Zapisano wyniki do pliku: {sciezka}")
