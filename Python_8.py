# PYTHON_8 — listy i krotki (tuples) w praktyce

# 1) Tworzenie listy i krotki
lista_dna = ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'G']
zasady_azotowe = ('Adenina', 'Tymina', 'Cytozyna', 'Guanina')

# 2) Pierwszy i ostatni element listy oraz krotki
print("Lista DNA - pierwszy:", lista_dna[0], "ostatni:", lista_dna[-1])
print("Zasady azotowe - pierwsza:", zasady_azotowe[0], "ostatnia:", zasady_azotowe[-1])

# 3) Modyfikacja elementu listy (krotki nie da się tak zmienić)
lista_dna[1] = 'U'  # np. zamiana 'T' na 'U' (pokazowo, jak w RNA)
print("Lista po modyfikacji:", lista_dna)

# zasady_azotowe[1] = "Uracyl"  # <-- To spowodowałoby błąd (krotka jest niemutowalna)

# 4) Dodanie elementu na końcu listy
lista_dna.append('A')
print("Lista po append('A'):", lista_dna)

# 5) Pętla for — przejście przez elementy listy i krotki
print("\nIteracja po liście:")
for nukleotyd in lista_dna:
    print(nukleotyd)

print("\nIteracja po krotce:")
for zasada in zasady_azotowe:
    print(zasada)

# 6) List comprehension — nowa lista na podstawie istniejącej (np. tylko puryny)
puryny = [n for n in lista_dna if n in ['A', 'G']]
print("\nPuryny z listy DNA:", puryny)
