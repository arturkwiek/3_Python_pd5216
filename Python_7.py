# PYTHON_7 — operatory w praktyce (bioinformatyczny klimat)

# 1) Zmienne boolean na podstawie warunków
sekwencja_dna = "ATGCGTACGATG"
dlugosc = len(sekwencja_dna)

czy_ma_start = sekwencja_dna.startswith("ATG")      # warunek: czy zaczyna się od kodonu start
czy_dluga = dlugosc >= 10                           # warunek: czy sekwencja ma co najmniej 10 nt
czy_aktywna = czy_ma_start and czy_dluga            # logiczne połączenie warunków

print("Czy sekwencja aktywna (start + długość>=10)?", czy_aktywna)

# 2) bool() — czy obiekt jest “pusty” (False) czy “niepusty” (True)
pusty_tekst = ""
lista_aa = ["Ala", "Gly"]
zero = 0
liczba_prob = 5

print("bool(pusty_tekst):", bool(pusty_tekst))
print("bool(lista_aa):", bool(lista_aa))
print("bool(zero):", bool(zero))
print("bool(liczba_prob):", bool(liczba_prob))

# 3) Operacje arytmetyczne: +, -, *, //, %
liczba_nukleotydow = 256
dodawanie = liczba_nukleotydow + 10
odejmowanie = liczba_nukleotydow - 50
mnozenie = liczba_nukleotydow * 2
kodony_pelne = liczba_nukleotydow // 3
reszta = liczba_nukleotydow % 3

print("\nArytmetyka:")
print("256 + 10 =", dodawanie)
print("256 - 50 =", odejmowanie)
print("256 * 2  =", mnozenie)
print("256 // 3 =", kodony_pelne)
print("256 % 3  =", reszta)

# 4) Operatory przypisania (modyfikacja istniejącej zmiennej)
liczba_mutacji = 100
liczba_mutacji += 5     # dodaj 5
liczba_mutacji *= 2     # podwój
liczba_mutacji //= 3    # podziel całkowicie przez 3

print("\nPo operacjach przypisania liczba_mutacji =", liczba_mutacji)

# 5) Operatory porównania
s1 = 150
s2 = 180

print("\nPorównania długości sekwencji:")
print("s1 < s2  :", s1 < s2)
print("s1 == s2 :", s1 == s2)
print("s1 > s2  :", s1 > s2)
print("s1 <= 150:", s1 <= 150)
print("s2 >= 200:", s2 >= 200)
