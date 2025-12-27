# PYTHON_15 — Pandas: DataFrame, NaN, filtrowanie, statystyki, eksport do CSV

import pandas as pd
import numpy as np

# 1) Utworzenie DataFrame
dane = {
    'Gen': ['GenA', 'GenB', 'GenC', 'GenD'],
    'Proba1': [5.1, 2.3, np.nan, 4.4],
    'Proba2': [3.2, 4.5, 3.9, np.nan],
    'Proba3': [6.3, 5.6, np.nan, 6.6]
}

df = pd.DataFrame(dane)
print("Oryginalny DataFrame:\n", df)

# 2) Sprawdzenie braków danych (NaN)
print("\nMiejsca z brakującymi wartościami (True = NaN):\n", df.isnull())

# 3) Usunięcie wierszy z brakami
df_bez_nan = df.dropna()
print("\nDataFrame po usunięciu wierszy z NaN:\n", df_bez_nan)

# 4) Uzupełnienie braków średnimi wartościami w kolumnach Proba1/2/3
srednie_kolumn = df[['Proba1', 'Proba2', 'Proba3']].mean()
df_uzupelnione = df.fillna(srednie_kolumn)
print("\nDataFrame po uzupełnieniu braków średnimi:\n", df_uzupelnione)

# 5a) Wyciągnięcie danych dla genu GenA
genA = df[df['Gen'] == 'GenA']
print("\nDane dla genu GenA:\n", genA)

# 5b) Średnia ekspresja dla każdej próby
srednia_proby = df[['Proba1', 'Proba2', 'Proba3']].mean()
print("\nŚrednia ekspresja w próbkach:\n", srednia_proby)

# 5c) Filtrowanie: geny z ekspresją w Proba1 > 4
wysoka_ekspresja = df[df['Proba1'] > 4]
print("\nGeny z ekspresją w Proba1 > 4:\n", wysoka_ekspresja)

# 6) Eksport do CSV (DataFrame po uzupełnieniu braków)
df_uzupelnione.to_csv("wynik.csv", index=False)
print("\nZapisano DataFrame (po uzupełnieniu braków) do pliku: wynik.csv")
