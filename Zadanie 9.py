import random

# Wylosuj liczbę od 1 do 100
liczba_do_zgadniecia = random.randint(1, 100)

# Zdefiniuj liczbę prób
ilosc_prob = 3

print("Witaj w grze w zgadywanie liczby!")
print("Zgadnij liczbę od 1 do 100. Masz tylko 3 próby.")

for proba in range(1, ilosc_prob + 1):
    # Prośba o podanie liczby przez użytkownika
    propozycja = int(input("Proszę podać liczbę: "))

    # Sprawdzenie czy liczba zgadnięta
    if propozycja == liczba_do_zgadniecia:
        print("Brawo! Zgadłeś liczbę w {} próbie!".format(proba))
        break
    elif propozycja < liczba_do_zgadniecia:
        print("Za mało.")
    else:
        print("Za dużo.")

# Wyświetlenie poprawnej odpowiedzi, jeśli użytkownik nie zgadł
if propozycja != liczba_do_zgadniecia:
    print("Niestety, nie udało się. Szukana liczba to:", liczba_do_zgadniecia)
