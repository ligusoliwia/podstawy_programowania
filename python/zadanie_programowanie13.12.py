#zadanie 4
while True:
    liczba1 = float(input('Podaj pierwszą liczbę: '))
    liczba2 = float(input('Podaj drugą liczbę: '))
    print('''Wybierz operację porównania:
          1. Większa niż
          2. Mniejsza niż
          3. Równa się
          4. Nie równa się''') #''' zachowuja edycje w tekscie
    
    wybor = input('Podaj numer operacji (lub wpisz "exit" aby zakończyć): ')
    if wybor == 'exit':
        break
    elif wybor == '1':
        wynik = liczba1 > liczba2
    elif wybor == '2':
        wynik = liczba1 < liczba2
    elif wybor == '3':
        wynik = liczba1 == liczba2
    elif wybor == '4':
        wynik = liczba1 != liczba2
    else:
        print('no cos nie pasuje mi tu, chyba zle wpisales cos, co nie??')
        continue
        
    print(f'omg oto twoje porownanie, fajne co nie?: {wynik}')

#zadanie 5
def sitoEratostenesa(n:int) -> list:
    if n < 2:
        return []

    czy_pierwsza = []
    for i in range(n + 1): #n + 1???
        czy_pierwsza.append(True) #t or f odpowiadaja czy liczba jest pierwsza czy nie, poczatkowo zak;adam ze wszystkie sa pierwsze
        
    czy_pierwsza[0] = False
    czy_pierwsza[1] = False #damn matma teoria bla bla bla

    p = 2
    while p * p <= n:
        if czy_pierwsza[p]:
            for multi in range(p * p, n + 1, p):
                czy_pierwsza[multi] = False
        p += 1

    wynik = []
    for i in range(2, n + 1):
        if czy_pierwsza[i]:
            wynik.append(i)
    return wynik


print(sitoEratostenesa(50))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]