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


lit = "wyraz"
lit = list(lit)
