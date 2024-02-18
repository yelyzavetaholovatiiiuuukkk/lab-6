import time

def sekundnik(czas):
    while czas >= 0:
        print("Pozostało", czas, "sekund.")
        time.sleep(1)
        czas -= 1

czas = int(input("Podaj czas w sekundach: "))
sekundnik(czas)
print("Koniec odliczania!")
