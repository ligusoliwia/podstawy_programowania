#DEFINIOWANIE I UŻYWANIE FUNKCJI FULL
#funkcja 'przechodzi' przez napisany kod tylko gdy jest wywołana, pomaga
#ominąć powtarzania tego samego kodu

#definiowanie funkcji: def nazwa_funkcji(argumenty funkcji):
#WAŻNE: funkcje nie mogą być puste (albo nie tworzyć ich, albo użyc 'pass'):
#przykład:
def wow():
    pass

#1.
#wywoływanie funkcji: nazwa_funkcji()
#stworzona funkcja sama w sobie jest tzw. obiektem pierwszoklasowym
#czyli nazwa tej funkcji wskazuje tylko na miejsce, gdzie zapisany jest kod
#wywołanie kodu funkcji musi odbyć się za pomocą nawiasów ()

def genesis():
    print('funkcja1: no son of mine')
    return 'funkcja1: invisible touch' #return tylko zwraca dane do programu
genesis() 
#takie wywołanie wyświetli to co jest zawarte w print()
get_return = genesis()
print(get_return)
#takie wywołanie wyświetli to co jest zawarte w print() oraz wartość zwróconą do programu
print(genesis()) #krótsza wersja tego co wyżej, nie trzeba tworzyć oddzielnej wartości

#2.
#tworzenie argumentów: def nazwa_funkcji(argument/y):
#argumenty to informacje przekazywane funkcji podczas wywoływania
#argumenty muszą być wywoływane w ten samej kolejności co zostały wpisane do funkcji
#przypisanie typów danych do argumentów: ...(argument: typ)
    #funkcje mogą przyjmować każdy typ jako argument
#można przypisać defaultowe wartości argumentów: ...(argument = default)
    #argumentu o defoultowej wartości nie trzeba wywoływać

def AM(song: str, year: int, albums, band = 'Arctic Monkeys'):
    print(f'funkcja2: piosenka \"{song}\" jest z {year} roku, od zespołu \"{band}\".')
    for album in albums:
        print(f'funkcja2: \"{album}\"')
albums = ['Humbug', 'AM', 'Whatever People Say I Am, I\'m Not', 'Suck It And See']
#funkcja przyjmuje całą listę i 'przetrwarza' ją w funkcji for
AM('Secret Door', 2009, albums)

#3.
#*args = tuple & **kwargs = dict
#funkcja ma ustalona ilosc argumentów, ale co jesli nie wiadomo ile ich bedzie?:

#ARBITARY ARGUMENT (*arg):
#przed argumentem *, np: def funkcja(*argument):
#zamiast jednego argumentu funkcja dostaje krotke (tuple)
#mozna dodać inne argumenty oprócz *arg:
def arg(control, *radio):
    print(f'''funkcja3: what the hell am i doin\' here! i\'m a {radio[1]} 
        (i don\'t belong here! cuz i\'m a {radio[2]}) but you\'re so {control}''')
arg( "special", "nutjob", "creep", "weirdo")

#ARBITARY KEYWORD ARGUMENT:
#przed argumentem **, np: def funkcja(**argument):
#tworzy slownik z argumentami
def smiths(**light):
    print(f"funkcja3: die by ur side {light["hev"]}, and so {light["ple"]}")
smiths(hev = "is a heavenly way to die", ple = "the pleasure is mine!")

#4.
#definiowanie dekoratora: def dekorator(funkcja)
#dekoratory dodają specjalne zachowania do funkcji, bez potrzeby zmiany jej kodu

#dekoratory to funkcje wyższego rzędu, czyli działają na innych funkcjach
#działają na zasadzie: nowa_funkcja = dekorator + og_funkcja

def body(funkcja): #argument to funkcja która będzie modyfikowana
    def paint(): #ta wewnętrzna funkcja zastąpi podaną oryginalną funkcję
        return funkcja().upper() #zwraca zmodyfikowaną oryginalną funkcję
    return paint #zwraca zastąpioną i zmodyfikowaną funkcję

@body #wywoływanie dekoratora i zaaplikowanie go na funkcję
def purple_rain():
    return 'funkcja4: yeahh!' #to tutaj jest aplikowana funkcja 'paint'
print(purple_rain()) #wyświetli nową, zmodyfikowaną funkcję

#jeśli chcemy udekorować funkcje która już istnieje gdzieś w kodzie:
genesis = body(genesis)
print(f'funkcja1_dekorator: {genesis()}')
#tutaj dekorator zadziała tylko na wartości zwrócone do programu w og funkcji
    #więc cokolwiek wpisane w print() nie zostanie udekorowane
    #czyli wynik: 
        #funkcja1: no son of mine
        #funkcja1_dekorator: FUNKCJA1: INVISIBLE TOUCH

#można dodawać wiele dekoratorów do funkcji:
def suit(funkcja):
    def vest():
        return funkcja() + '... tutaj przykład wielu dekoratorów'
    return vest
@body
@suit
def just():
    return 'funkcja4_dekorator: radiohead propaganda'
print(just())

#5.
#SUPER MEGA ULTRA WAŻNE: rekurencja, czyli kiedy funkcja wywołuje samą siebie
#rekurencje są ryzykowne, bo niepoprawnie użyte moga spowodować zawieszenie programu
    #niezbędne elementy, żeby rekurencja zadziałała: warunek stop oraz krok rekurencyjny
def liczenie(n):
    if n <= 0:
        print('funkcja5: hihihaha, liczenie skończone (twoje dni są policzone)')
    else:
        print(n)
        liczenie(n - 1)
liczenie(4)
#kroki -> działanie rekurencji:
    #4 nie jest mniejsze od zera
    #więc wyświetla 4 i wywołuje funkcję liczenia jeszcze raz, ale dla 4 - 1 = 3
#kroki są powtarzane dopółki warunek stop (n <= 0) jest spełniony

#INNY PRZYKŁAD REKURENCJI: sekwencja fibonacciego:
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
print(f'funkcja5: {fib(10)}')

#INNY PRZYKŁAD REKURENCJI: zliczanie elementów w liście:
def sum_list(num):
  if len(num) == 0:
    return 0
  else:
    return num[0] + sum_list(num[1:])
cyferki = [1, 2, 3, 4, 5]
print(f'funkcja5: {sum_list(cyferki)}')

#python ma ograniczoną ilość rekurencji (około 1000 wywołań)
#można sprawdzić to za pomocą:
    #import sys
    #print(sys.getrecursionlimit())
#oraz zmienić za pomocą:
    #sys.setrecursionlimit(ilość rekurencji)