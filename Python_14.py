# PYTHON_14 — NumPy: macierz ekspresji genów + operacje + NaN

import numpy as np

# 1) Macierz ekspresji: 4 geny (wiersze) x 3 próby (kolumny)
macierz_ekspresji = np.array([
    [5.0, 2.5, 7.0],
    [3.2, 4.0, 6.0],
    [8.1, 9.3, 2.5],
    [4.5, 5.7, 6.9]
])

print("Macierz ekspresji (4 geny x 3 próby):\n", macierz_ekspresji)

# 2a) Zwiększenie ekspresji wszystkich genów o 5%
ekspresja_plus_5 = macierz_ekspresji * 1.05
print("\nEkspresja po zwiększeniu o 5%:\n", ekspresja_plus_5)

# 2b) Średnia ekspresja dla każdego genu (axis=1 -> wzdłuż wierszy)
srednia_geny = np.mean(macierz_ekspresji, axis=1)
print("\nŚrednia ekspresja dla każdego genu:\n", srednia_geny)

# 2c) Suma ekspresji genów dla każdej próby (axis=0 -> wzdłuż kolumn)
suma_proby = np.sum(macierz_ekspresji, axis=0)
print("\nSuma ekspresji genów dla każdej próby:\n", suma_proby)

# 3) Wprowadzenie braków danych (NaN)
macierz_z_nan = macierz_ekspresji.copy()
macierz_z_nan[0, 2] = np.nan   # brak w genie 1, próba 3
macierz_z_nan[1, 1] = np.nan   # brak w genie 2, próba 2
macierz_z_nan[3, 0] = np.nan   # brak w genie 4, próba 1

print("\nMacierz z brakującymi danymi (NaN):\n", macierz_z_nan)

# 4) Średnia ekspresja genów z pominięciem NaN
srednia_geny_bez_nan = np.nanmean(macierz_z_nan, axis=1)
print("\nŚrednia ekspresja dla każdego genu (ignorując NaN):\n", srednia_geny_bez_nan)
