# PYTHON_10 — funkcje, argumenty nazwane + **kwargs

def charakterystyka_bialka(*, sekwencja, masa, pI):
    """
    Zwraca sformatowany opis białka.
    Wszystkie argumenty są keyword-only (wymuszone przez '*').
    """
    return (
        f"Charakterystyka białka:\n"
        f"\tSekwencja: {sekwencja}\n"
        f"\tDługość: {len(sekwencja)} aa\n"
        f"\tMasa: {masa} Da\n"
        f"\tpI: {pI}"
    )


def sumuj_cechy_bialek(**kwargs):
    """
    Przyjmuje dowolną liczbę nazwanych cech białek w stylu:
    masa_<nazwa>=..., pI_<nazwa>=...
    Zwraca: (suma_mas, srednie_pI)
    """
    masy = [v for k, v in kwargs.items() if k.startswith("masa_")]
    pI_wartosci = [v for k, v in kwargs.items() if k.startswith("pI_")]

    suma_mas = sum(masy)
    srednie_pI = sum(pI_wartosci) / len(pI_wartosci) if pI_wartosci else 0

    return suma_mas, srednie_pI


# --- Przykładowe użycie ---

opis = charakterystyka_bialka(sekwencja="MAKVTS", masa=574.0, pI=5.2)
print(opis)

suma_mas, srednie_pI = sumuj_cechy_bialek(
    masa_hemoglobina=64500.0, pI_hemoglobina=6.8,
    masa_albumina=66400.0, pI_albumina=4.7
)

print("\nPodsumowanie cech białek:")
print(f"\tSuma mas: {suma_mas} Da")
print(f"\tŚrednie pI: {srednie_pI}")
