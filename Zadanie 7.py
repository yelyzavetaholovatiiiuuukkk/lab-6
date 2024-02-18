import random
from math import prod

# Funkcja obliczająca średnią geometryczną
def srednia_geometryczna(krotka):
    iloczyn = prod(krotka)
    return iloczyn ** (1 / len(krotka))

# Pobranie przedziału od użytkownika
poczatek = int(input("Podaj początek przedziału: "))
koniec = int(input("Podaj koniec przedziału: "))

# Losowanie elementów do krotki
krotka = tuple(random.randint(poczatek, koniec) for _ in range(10))

print("Wylosowana krotka:", krotka)

# Obliczenie średniej geometrycznej
srednia_geo = srednia_geometryczna(krotka)
print("Średnia geometryczna krotki:", srednia_geo)
