#podstawy: typy danych, zmienne, listy etc

#funkcja(parametry), jesli nie ma parametrow to pusty nawias

#typy proste
#int - calkowita
#float - zmiennoprzecinkowa, 
#str (string) - tekst
#bool (boolean) - True/ False 

#definicja zmiennej: nazwa_zmiennej = wartość
    #spacje w nazwach zmiennych to _
    #dokladnie nazwywac zmienne

#typy złożone
#krotka - lista wartości po przecinkach, nie można modyfikowac > stałe dane
krotka = (1, 2, 3, 4, "lol", False)
print(krotka)
#lista - lista wartości po przecinkach, można modyfikowac
lista = [1, 2, "hihi", True]
print(lista)
#zbiór - lista unikalnych wartosci, usuwa duplikaty
#slownik - #po lewej klucz, po prawej wartosc, 
    #oba jako wartosci tekstowe (str), po dwukropku
slownik = {
    "a": "ananas",
    "b": 2,
}
print(slownik)
slownik.get("a") #odwolanie sie do slownika, '.get' to metoda funkcji
print(slownik.get("a"))

#LISTY
print(lista[0]) #odwolanie do wartosci z listy nazwa_zmiennej[index]
lista[0] = 3 #zmiana wartosci listy dla danego indexu
print(lista[0])
lista_zmienna = lista[2] #tworzenie zmiennej pomocniczej
print(lista_zmienna) #żeby przy każdej opercaji nie odwolywac sie 
#bezposrednio do listy to tworzy sie zmienna pomocnicza
lista[2] = "bleh" #zmienna pomocnicza nie jest zalezna od listy
#nie zmienia sie dynamicznie
print(lista_zmienna) #to wciaz pokaze "hihi" nie zmieni sie na nowa wartosc
#z listy :)
print(lista[-1]) #zwraca indexy od tylu '-1' to ostatnia wartosc listy
    #inaczej:
    #index = len(lista) - 1
    #print(lista[index])
print(lista[1:3]) #zwraca przedzial, wlacznie z pierwszym indexem
#wylacznie z drugim podanym indexem
print(lista[2:]) #zostawione puste zwraca wartosci od pierwszego indexu
#do konca - mozna na odwrot ' :3'
index = len(lista) - 1
print(lista[index])

lista.append(3) #dodaje na koniec listy podana wartosc
print(lista)

lista.insert(1, "miua") #dodaje podana wartosc na podany index w liscie
print(lista)

lista.remove("bleh") #usuwa podana wartosc z listy
print(lista)

lista.pop(0) #usuwa wartosc z podanego indexu
print(lista)

lista.clear() #usuwa wartosci z listy
print(lista)

#konwersja na inny system liczbowy
a = 10
print(bin(a))
#bin - binarny
#oct - osemkowy
#hex - szesnastkowy
#int - dziesiatkowy

h = True if 20 > 10 else False

if 20 > 10:
    naj = "ff"
else:
    naj = "hh"

#przechodzi przez liste, 'liczba' to podstawione kolejne wartosci
lista_liczb = [1, 2, 3, 4]

for liczba in lista_liczb:
    if liczba > 2:
        print(liczba)

#odwracanie wyrazu
wyraz = "abcd"
odwrotnosc = ""

for i in range(len(wyraz)):
    index = (len(wyraz) - 1) - i #zmniejszam i bo pisze str od tylu
    #odejmuje 1 bo len daje dlugosc tablicy a nie ostatni index
    odwrotnosc += wyraz[index] #dodaje kolejne wartosci do nowej listy
print(odwrotnosc)

#range(start, stop, step) - wlacznie z start, bez stop
for i in range(20, 100, 10):
    print(i)

#konwersja typow danych
lit = "wyraz"
lit = list(lit)

meg = [1, 2, 2, 3, 4, 4, 4]
print(list(set(meg))) #to samo da się dwoma for loopami w sobie

#FUNKCJE
def vol(x: int, y: int) -> int:
    if x == 1 or y == 1:
        return "fsgs"
    return x + y

o = 10
wynik1 = vol(o,5)

x = 'string'
y = 14.3
z = 3
a = True
print(type(x))
print(type(y))
print(type(z))
print(type(a))

conv = float(z)
print(type(conv))

unpacking = ('the', 'end', 'is', 'near')
a, b, c, d = unpacking
print(unpacking)
print(b)

import random
print(random.randrange(1,9)) #printuje random liczbe w range 1-9

chasing = 'pavements'
print(chasing[0])
#or print(chasing[2:4]) #range indexow 

up = 'i\'ll die on this hill' #slash pozwala na wpisanie w str cudzyslowia bez wypluwania bledu
print(up.upper())

down = 'NOTHING COULD MATTER'
print(down.lower())

spl = 'i wish, something could matter to you'
print(spl.split(","))

combo = up + ", " + down + ", " + spl
print(combo.lower())

mon = 9
txt = f'the price for ur soul is: {mon:.2f} monopoly money, good luck!'
print(txt)

import random
x = random.randrange(0,10)
y = random.randrange(0,10)
if x > y:
    print(True)
else:
    print(False)

print(f"{15%4}")
miau = 15%4
print(miau)
print(meow:=12%4)

nums = [1,2]
count = len(nums)
if count > 3:
    print(f'ur list is {count} lomng')
if (count := len(nums)):
    print(f'ur list is {count} lomng')

favsGA = ['tangerine', 'domestic bliss', 'ur love(deja vu)']
favsAM = ['no.1 party anthem', '505', 'certain romance']
fvGA = favsGA
print(favsGA is favsAM)
print(fvGA is favsGA)
print(favsAM is not favsGA)
print('tangerine' in favsGA)
print('505' not in favsAM)

tangerine = ["tastey"]
brain = ["got", "cuz", "i\'m"]
#brain[0] = [" "] #zamienia podane indexy
brain.append("braindead")
brain.insert(1, "nobody")
print(brain)
brain.extend(tangerine)
print(brain)
brain.sort()
print(brain)
numnom = [1, 2, 7, 1212, 55, 3, 23, 994, 1000 , 302, 203]
numnom.sort()
print(numnom)
numnom.sort(reverse = True)
print(numnom)
brain.reverse()
print(brain)

rah = {
    "artist": "deaftones",
    "genre": "alt rock",
    "track": "sextape"
}
print(rah["genre"])
print(len(rah))

#obsluga bledow z try i except
#try - testuje na bledy
#except - instrukcja jesli blad
#else - instr jesli nie ma bledu
#finally - instr wykona sie niezaleznie od wyniku try i except
#try:
    #print(cos) zmienna nie istnieje
#except:
#   print("nothing to print (no ink!!)")
#else:
#   print("all good")
#finally:
#   print("hihi, try again")

#wypluwanie bledow!
#x = 5
#if x > 2:
    #raise ValueError("sorry not sorry, wrong number")

#puste // none
x = None
print(x)
#porownywanie z is i is not
result = None
if result is None:
    print("nothing to see yet dear")
else:
    print("ready as i\'ll ever be!")