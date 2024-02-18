import random

def losowanie_totolotka():
    lista_liczb = list(range(1, 50))
    wylosowane = random.sample(lista_liczb, 6)
    return sorted(wylosowane)

wylosowane_liczby = losowanie_totolotka()
print("Wylosowane liczby w totolotku:", wylosowane_liczby)
