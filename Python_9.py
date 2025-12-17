# PYTHON_9 — zbiory (set), słowniki (dict) + instrukcje warunkowe

# 1) Zbiór unikalnych elementów oraz słownik gen->funkcja
aminokwasy = {"Gly", "Ala", "Val"}  # set: unikalne aminokwasy
geny = {
    "BRCA1": "naprawa DNA",
    "TP53": "regulacja cyklu komórkowego",
    "EGFR": "sygnalizacja wzrostu"
}

# 2) Dodanie elementu do zbioru i pary klucz-wartość do słownika
aminokwasy.add("Leu")
geny["MYC"] = "regulacja transkrypcji"

# 3) Sprawdzenie przynależności: element w zbiorze, klucz w słowniku
print("Czy 'Leu' jest w zbiorze aminokwasy?", "Leu" in aminokwasy)
print("Czy 'BRCA2' jest kluczem w słowniku geny?", "BRCA2" in geny)

# 4) Usunięcie elementu ze zbioru (discard nie robi błędu, jeśli elementu nie ma)
aminokwasy.discard("Val")
print("Zbiór po usunięciu 'Val':", aminokwasy)

# 5) Wyświetlenie zawartości słownika: klucze i wartości (pętla for)
print("\nSłownik geny (klucz -> wartość):")
for gen, funkcja in geny.items():
    print(gen, "->", funkcja)

# 6) if-else: sprawdzenie długości zbioru
if len(aminokwasy) > 3:
    print("\nZbiór aminokwasy zawiera więcej niż 3 elementy.")
else:
    print("\nZbiór aminokwasy zawiera 3 lub mniej elementów.")

# 7) Instrukcja warunkowa: jeśli klucz istnieje, wyświetl jego wartość
szukany_gen = "TP53"
if szukany_gen in geny:
    print(f"Wartość dla klucza '{szukany_gen}':", geny[szukany_gen])
else:
    print(f"Klucz '{szukany_gen}' nie istnieje w słowniku geny.")

# 8) Łączenie zbiorów (union) i wydruk wyniku
inne_aminokwasy = {"Ser", "Thr", "Ala"}  # Ala się powtarza, więc union i tak zostawi ją raz
polaczone = aminokwasy.union(inne_aminokwasy)

print("\nZbiór 1:", aminokwasy)
print("Zbiór 2:", inne_aminokwasy)
print("Union (połączone):", polaczone)
