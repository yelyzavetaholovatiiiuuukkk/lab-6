import math


def pole_trojkata_ostrokatnego(a, b, kat):
    # Sprawdzenie czy trójkąt istnieje
    if a + b <= kat or a + kat <= b or b + kat <= a:
        print("Trójkąt o bokach {} i {} oraz kącie {} stopni nie istnieje.".format(a, b, kat))
        return None

    # Sprawdzenie czy trójkąt jest ostrokatny
    if kat >= 90:
        print("Trójkąt o kącie {} stopni nie jest ostrokatny.".format(kat))
        return None

    # Obliczenie pola trójkąta ostrokatnego
    kat_radiany = math.radians(kat)
    pole = 0.5 * a * b * math.sin(kat_radiany)
    return pole


# Testowanie funkcji
a = float(input("Podaj długość pierwszego boku trójkąta: "))
b = float(input("Podaj długość drugiego boku trójkąta: "))
kat = float(input("Podaj szerokość kąta ostrego pomiędzy bokami (w stopniach): "))

pole = pole_trojkata_ostrokatnego(a, b, kat)
if pole is not None:
    print("Pole trójkąta ostrokatnego wynosi:", pole)
