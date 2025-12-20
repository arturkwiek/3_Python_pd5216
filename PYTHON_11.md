# PYTHON_11 — Programowanie obiektowe (OOP): klasy, dziedziczenie, super(), metoda statyczna

class Organizm:
    def __init__(self, nazwa, rodzaj):
        self.nazwa = nazwa
        self.rodzaj = rodzaj

    def opisz(self):
        return f"Organizm: {self.nazwa} (rodzaj: {self.rodzaj})"

    @staticmethod
    def transkrybuj(sekwencja_dna):
        # Zamiana DNA -> RNA (T -> U)
        return sekwencja_dna.replace("T", "U")


class Bakteria(Organizm):
    def __init__(self, nazwa, rodzaj, ksztalt):
        super().__init__(nazwa, rodzaj)
        self.ksztalt = ksztalt

    def opisz(self):
        opis_bazowy = super().opisz()
        return f"{opis_bazowy}, kształt: {self.ksztalt}"


# --- Testy (wymagane) ---

b1 = Bakteria("Escherichia coli", "bakteria", "pałeczka")
b2 = Bakteria("Staphylococcus aureus", "bakteria", "ziarniak")
b3 = Bakteria("Spirillum volutans", "bakteria", "spiralna")

print(b1.opisz())
print(b2.opisz())
print(b3.opisz())

sekwencja_dna = "ATGCTTACG"
sekwencja_rna = Organizm.transkrybuj(sekwencja_dna)

print("\nTranskrypcja DNA -> RNA:")
print("DNA:", sekwencja_dna)
print("RNA:", sekwencja_rna)
