import datetime

def dzien_roku(rok, miesiac, dzien):
    data = datetime.date(rok, miesiac, dzien)
    return data.timetuple().tm_yday

def numer_tygodnia(rok, miesiac, dzien):
    data = datetime.date(rok, miesiac, dzien)
    return data.isocalendar()[1]

def data_przed_i_po(rok, miesiac, dzien):
    data = datetime.date(rok, miesiac, dzien)
    data_przed = data - datetime.timedelta(days=14)
    data_po = data + datetime.timedelta(days=14)
    return data_przed, data_po

def najblizsza_niedziela(rok, miesiac, dzien):
    data = datetime.date(rok, miesiac, dzien)
    dni_do_niedzieli = 6 - data.weekday()
    if dni_do_niedzieli == 0:
        dni_do_niedzieli = 7
    data_niedziela = data + datetime.timedelta(days=dni_do_niedzieli)
    return data_niedziela

def czas_unixowy(rok, miesiac, dzien):
    data = datetime.datetime(rok, miesiac, dzien)
    return int(data.timestamp())

# Pobranie danych od użytkownika
rok = int(input("Podaj rok: "))
miesiac = int(input("Podaj miesiąc: "))
dzien = int(input("Podaj dzień: "))

# Obliczenie i wyświetlenie wyników
print("Dzień roku:", dzien_roku(rok, miesiac, dzien))
print("Numer tygodnia:", numer_tygodnia(rok, miesiac, dzien))
data_przed, data_po = data_przed_i_po(rok, miesiac, dzien)
print("Data na 2 tygodnie przed:", data_przed)
print("Data na 2 tygodnie po:", data_po)
print("Najbliższa niedziela:", najblizsza_niedziela(rok, miesiac, dzien))
print("Czas unixowy bieżącej godziny w podanym dniu:", czas_unixowy(rok, miesiac, dzien))
