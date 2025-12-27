# biology.py
from collections import Counter

def opis_komorki():
    return "Komórka to podstawowa jednostka życia"

def licz_nukleotydy(sekwencja):
    """
    Zlicza nukleotydy A/T/C/G w sekwencji DNA i zwraca obiekt Counter.
    """
    sekwencja = sekwencja.strip().upper()
    return Counter(sekwencja)
