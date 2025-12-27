# PYTHON_16 — Wizualizacja danych (Matplotlib): line plot, bar plot, scatter + zapis do PNG

import numpy as np
import matplotlib.pyplot as plt

# 1) Przygotowanie danych
geny = ['GenA', 'GenB', 'GenC']
proby = ['Proba1', 'Proba2', 'Proba3']

ekspresja = np.array([
    [5.1, 2.3, 7.8],  # GenA
    [3.2, 4.5, 6.1],  # GenB
    [4.8, 5.5, 3.9]   # GenC
])

# 2a) Wykres liniowy (line plot)
plt.figure(figsize=(7, 4))
for i, gen in enumerate(geny):
    plt.plot(proby, ekspresja[i], marker='o', label=gen)

plt.title('Zmiany ekspresji genów w próbkach (line plot)')
plt.xlabel('Próbki')
plt.ylabel('Ekspresja')
plt.legend(title="Geny")
plt.grid(True)
plt.tight_layout()

# Zapis jednego wykresu do PNG (wymagane)
plt.savefig("ekspresja_genow.png")
plt.show()

# 2b) Wykres słupkowy (bar plot)
plt.figure(figsize=(7, 4))
width = 0.25
x = np.arange(len(proby))

for i, gen in enumerate(geny):
    plt.bar(x + i * width, ekspresja[i], width, label=gen)

plt.xticks(x + width, proby)
plt.title('Porównanie ekspresji genów w próbkach (bar plot)')
plt.xlabel('Próbki')
plt.ylabel('Ekspresja')
plt.legend(title="Geny")
plt.tight_layout()
plt.show()

# 2c) Wykres rozrzutu (scatter plot): GenA vs GenB
plt.figure(figsize=(6, 4))
plt.scatter(ekspresja[0], ekspresja[1], marker='x')
plt.title('Porównanie ekspresji GenA i GenB (scatter)')
plt.xlabel('Ekspresja GenA')
plt.ylabel('Ekspresja GenB')
plt.grid(True)
plt.tight_layout()
plt.show()

print("Zapisano wykres do pliku: ekspresja_genow.png")
