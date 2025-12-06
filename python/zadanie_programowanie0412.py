# kod zadanie 1
liczby = []
while True:
    tekst = input('podaj liczbę całkowitą lub wpisz "stop" aby zakończyć: ')
    if tekst == 'stop':
        break
    else:
        liczby.append(int(tekst))

print(f'twoje liczby: {liczby}')

# kod zadanie 2
def srednia(lista_liczb) -> float:
    #-> deklaruje typ zmiennej, funkcja def jest zdefiniowana jako zmiennoprzecinkowa, python nie wymaga 
    suma = 0 #początkowe ustalenie sumy na 0, potem dodawane elementy
    for liczby in lista_liczb: #użycie for in: nie znam ilości wartości
        suma += liczby #dodawanie wartości do sumy
    return suma / len(lista_liczb) #suma / ilość elementów

print(f'średnia z podanych liczb: {srednia(liczby)}')

# kod zadanie 3
def parzyste(lista_liczb): #stworzenie funkcji
    liczby_parzyste = [] #deklaracja zmieneej
    czy_parzyste = False #deklaruje zmienna, opcje true or false (ale na poczatku tylko jedna opcje potem zmieniac)
    #aktualnie kod mysli ze wszystkie sa parzyste
    for liczby in lista_liczb: #for, bo nie znam ilości wartości w liście
        if liczby%2==0: #sprawdza parzystość
            liczby_parzyste.append(liczby) #dodaje wartości parzyste do listy
            czy_parzyste=True
    if czy_parzyste==False: #= zmiana wartosci == porownanie wartosci
        return 'brak parzystych' #return tekst, zwraca zmienna ale jej nie wyswietla bez printa
    else:
        return liczby_parzyste
print(parzyste (liczby))