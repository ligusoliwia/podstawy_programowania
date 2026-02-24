#ZADANIE 1 i 2
def NWD(a, b) -> float:
    while True:
        if a % b == 0:
            return b
        else:
            a, b = b, a % b

def NWW(a, b) -> float:
    return (a*b)/NWD(a,b)

while True:
    a = int(input('proszę podaj pierwszą liczbę: '))
    b = int(input('proszę podaj drugą liczbę: '))
    wynik = NWW(a,b)
    x = input(f'NWW wynosi: {wynik}, czy chcesz kontynuować? tak/nie: ')
    if x == 'nie':
        break

#ZADANIE 3
def SILNIA(n):
    wynik = 1
    for i in range(1, n + 1): #n+1 bo wyłącza ostatni wyraz
        wynik = wynik * i
    return wynik

print(SILNIA(4))

#ZADANIE 4
def FIB(num) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return FIB(num - 1) + FIB(num - 2) #rekurencyjna = wywołuje samą siebie
wynik = FIB(5)
print(wynik)

#ZADANIE 5
tabm = []
def TAB() -> int:
    for i in range (1,11):
        for n in range(1,11):
            tabm.append(i*n)
TAB()
print(tabm)

#ZADANIE 6
def D(num):
    suma_dziel = 0
    #poszukać dzielników od 1 do połowy liczby
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            suma_dziel += i
    if suma_dziel == num:
        return True
    else:
        return False

def LSD(n):
    x = 0
    liczba = 2
    while x < n:
        if D(liczba):
            print(f"liczba doskonała: {liczba}")
            x += 1
        liczba += 1

LSD(3)

#ZADANIE 7
def SC() -> int:
    while True:
        num = input('wpisz liczbę naturalną: ')
        wow = len(num)
        con = input(f'ilość cyfr w twojej liczbie to {wow}, czy chcesz kontynułować? tak/nie: ')
        if con == 'nie':
            break

SC()

#ZADANIE 8
def MM(lista, tryb) -> float:
    if tryb.lower() == 'max':
        return max(lista)
    elif tryb.lower() == 'min':
        return min(lista)

t = input('proszę wybierz tryb; max/min: ')
l = input('proszę podaj swoją listę liczb: ')
nums = [float(x) for x in l.split()]
    
if not nums:
    print('nie podano żadnych liczb, próbuj dalej')
else:
    wynik = MM(nums, t)
    print(f"twój wynik dla trybu {t}: {wynik}")

#ZADANIE 9 - odwrotność liter
fraza = input('proszę wprowadź swój dowolny napis: ')
odwrotnosc = fraza[::-1]
print(odwrotnosc)

#ZADANIE 9.5 - odwrotność słów
napis = input("proszę wprowadź swój dowolny napis: ")
slowa = napis.split()
slowa_odwrocone = slowa[::-1]
wynik = " ".join(slowa_odwrocone) #połączenie, oddzielonie słów spacją
print(wynik)

#ZADANIE 10
def PALINDR(napis) -> str:
    slowa = napis.split()
    laczenie = "".join(slowa) #slowo bez spacji
    laczenie_odwr = laczenie[::-1]
    if laczenie == laczenie_odwr:
        return True
    else:
        return False

wyraz = input('proszę podaj wyraz który chcesz sprawdzić: ')
print(PALINDR(wyraz))
