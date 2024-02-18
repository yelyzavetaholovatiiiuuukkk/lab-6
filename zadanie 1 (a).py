import random

def losuj_szczesliwy_numerek(grupa):
    return random.choice(grupa)

grupa_osob = ['Bożena', 'Sebastian', 'Yelyzaveta', 'Kamil', 'Yuliia']
szczesliwy_numerek = losuj_szczesliwy_numerek(grupa_osob)
print("Szczęśliwy numerek dla grupy:", szczesliwy_numerek)
