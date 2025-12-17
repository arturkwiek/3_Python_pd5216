# Program demonstrujący typy danych i konwersję typów w Pythonie
# Przykład na sekwencji DNA

sekwencja_dna = "ATGCGTAC"          # Zmienna typu str (ciąg znaków)
print(sekwencja_dna, type(sekwencja_dna))  # Wyświetlenie wartości i typu w jednej linijce

sekwencja_dna = list(sekwencja_dna) # Konwersja typu str na list
print(sekwencja_dna, type(sekwencja_dna))  # Ponowne wyświetlenie wartości i typu

# Przykładowe użycie funkcji range()
for i in range(len(sekwencja_dna)):
    print("Pozycja", i, ":", sekwencja_dna[i])
