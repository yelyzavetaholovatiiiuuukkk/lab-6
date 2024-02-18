import random

def losuj_szczesliwy_rocznik():
    return random.randint(2005, 2006)

grupa_osob = ['Bożena', 'Sebastian', 'Yelyzaveta', 'Kamil', 'Yuliia']
roczniki = [losuj_szczesliwy_rocznik() for _ in range(len(grupa_osob))]
print("Roczniki urodzenia w grupie:", roczniki)
