#OOP - object-oriented programming
#klasy troche jak przepis dla obiektow/ blueprint dla obiektow
#klasa definiuje strukture i zachowanie jej obiektow
#obiekty dziedzicza ze swojej klasy (typ danych etc)
#np: klasa: samochody obiekty: mcqueen, dinoking maruchalol
class paramore:
    x = 2 #ta własność nalezy do klasy
    z = 4

after_laughter = paramore() #stworzony obiekt
print(after_laughter.x) #x staje sie metoda dla argumentu klasy

#konstruktor init: pozwala na wpisanie poczatkowych wartosci dla atrybutow obiektu
class sinatra:
    def __init__(self, name, fav_track):
        self.name = name #ta własność nalezy juz do obiektu
        self.fav_track = fav_track

spofifi = sinatra("frank", "strangers in the night") #stworzony obiekt
#mozna modyfikowac argumenty
spofifi.name = "Frank"
#mozna usuwać argumenty
del spofifi.fav_track
print(spofifi.name)
#print(spofifi.fav_track) --> to wypluje blad

#magiczne self - o co chodzi i czemu jest wszedzie?
#self to argument ktory pozwala na dostep do wlasciwosci i metod klasy
#kieruje co gdzie wpisac
#self.name w klasie = spofifi.name w wywolaniu klasy => dany obiekt jest podstawiany pod self

#!! WAZNE: self nie musi sie tak nazywac (ale to norma), to moze byc cokolwiek, 
#ale musi byc pierwsze jako argument funkcji konstruktora
class ABBA:
    def __init__(self, album, track):
        self.album = album
        self.track = track
    
    def abba_info(self):
        print(f"here\'s ur info: {self.album} and {self.track}, have fun lol!")
    
faves = ABBA("Abba", "Mama Mia")
ohgod = ABBA("Super Trouper", "The Winner Takes It All")

print("my fav is: " + faves.album)
print(f"the one i cried the most is: {ohgod.track} lol")

#self mozna tez wywolywac metody:
class TheSmiths:
    def __init__(self, album, track):
        self.album = album
        self.track = track
    
    def hello(self):
        return "hi, your coolest track is: " + self.track
    
    def greet(self):
        message = self.hello()
        print(message + f"!! it's from \"{self.album}\" album")
    
tutu = TheSmiths("Hatfull of Hollow", "Heaven Knows I\'m Miserable Now")
tutu.greet()

#zmiana własności obiektu zmienia tylko obiekt, ale zmiana własności klasy zmienia to dla wszystkich obiektów 
class fool:
    species = ""

    def __init__(self, name):
        self.name = name

prsn = fool("diana")
print(prsn.name)

fool.species = "human" #zamienia własność całej klasy
print(prsn.species)

#mozna dodawac nowe własności do obiektow
prsn.age = 22
prsn.track = "dirty diana"
print(prsn.age)

class rox:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self): #__str__ to metoda kontrolujaca co jest zwracane jesli wyswietlane
    #str pozwala na ladne wyswietlenie dla usr
    return f"{self.name} is {self.age}"

woow = rox("roxanne", 19)
print(woow)

#DZIEDZICZENIE (EGZOGENNE KLASOWE lol)

#jest sobie jakas smieszna klasa:
class the_police:
    def __init__(self, track, album, year):
        self.track = track
        self.album = album
        self.year = year
    
    def ink(self): #stworzenie metody
        print(f"alr so... {self.track} is from {self.album} album, from {self.year}, cool right?")

song_one = the_police("Every Breath You Take", "Synhronicity", 1983)
song_one.ink()

class faves(the_police): #stworzenie dzieciaka (klasy dziedziczacej)
    pass #nie moze stac pusta, bedzie automatycznie dziedziczyc od rodzica (the police)
song_two = faves("Message In A Bottle", "Reggatta De Blanc", 1979)
song_two.ink() #wyswietli dokladnie tak jak w klasie z ktorej dziedziczy

#ALE UWAGA HIHI: jesli doda sie metode __init__ do dzieciaka, nie bedzie on juz dluzej dziedziczyc z nadrzednej klasy
class orphan(the_police):
    def __init__(self, track, album, year, composer): #nowy konstruktor nadpisuje ten dziedziczony, klasa ma inne wlasnosci
        super().__init__(track, album, year) #super() spowoduje dziedziczenie od nadrzednej klasu (the police)
        #u dzieciaka mozna dodawac nowe własnosci, trzeba pamietac o dopisaniu ich do konstruktora
        self.composer = composer
    def ink_upgrade(self):
        print(f'''alr so... {self.track} is from {self.album} album, from {self.year}, 
              the composer of this masterpiece is {self.composer}, cool right?''')
    #UWAGA jesli metoda dzieciaka bedzie sie nazywac tak samo jak u rodzica,
    #to metoda rodzica zostanie nadpisana

song_three = orphan("Roxanne", "Outlandos D\'Amour", 1978, "Sting")
song_three.ink_upgrade()

#polymorfizm? co jesli kilka klas ma taka sama metode?

class food:
    def __init__(self, taste, size):
        self.taste = taste
        self.size = size
    def change(self):
        print(f"HAVE A GOOD {(self.taste).upper()} MEAL DUDE!")

class sleep:
    def __init__(self, bed, time):
        self.bed = bed
        self.time = time
    def change(self):
        print(f"HAVE A GOOD {(self.time).upper()} SLEEP DUDE!")

class drink:
    def __init__(self, type, colour):
        self.type = type
        self.colour = colour
    def change(self):
        print(f"HAVE A GOOD {(self.type).upper()} DRINK DUDE!")

#mozna przeiterowac sie przez wszystkie po kolei:
#pierwsze stworzyc obiekty
fish = food("sour", "small")
nap = sleep("kingsize", "2hrs")
tea = drink("warm", "black")
#potem loop z metoda
for i in (fish, nap, tea):
    i.change()

#OCHRONA DANYCH?? (nikt chyba nie kradnie takich rzeczy, nacisk na chyba)

class DianaRoss:
    def __init__(self, track, album):
        self._track = track
        self.album = album
#nie da sie dostac wartosci jesli nie ma wpisanej takiej metody do klasy
    def get_sth(self):
        return self._track
#mozna edytowac wartosci prywatne klasy metoda set
    def set_sth(self, track):
        self._track = track
song1 = DianaRoss("Upside Down", "Diana")
print(song1.album)
#print(song1.track) #to wypluje blad!, ale jesli doda sie _ to print zadziala
print(song1._track) #wow

print(song1.get_sth()) #zobaczenie prywatnej wartosci za pomoca metody wpisanej w klase

song1.set_sth("I\'m Coming Out") #zmiana wartosci prywatnej za pomoca metody klasy
print(song1._track)

#KLASY WEWNETRZNE
class outer_wilds:
    def __init__(self):
       self._name = "shell"
    
    class inner_wilds:
        def __init__(self):
            self._name = "core"

        def where(self):
            print("u are in the core lol")

planet_shell = outer_wilds()
print(planet_shell._name) #wyswietli cokolwiek w zewnetrzznej klasie
planet_core = planet_shell.inner_wilds()
print(planet_core._name) #wyswietli cokolwiek w wewnetrznej klasie
planet_core.where() #wyswietli funkcje w wewnetrznej klasie

#zewnetrzne klasy maja defaultowo dostep do wewnetrznych, ale nie na odwrot
#zeby wewnetrzna miala dostep do zewnetrznej, musi miec to podane jako argument
#przyklad z w3sql:
class Outer:
  def __init__(self):
    self.name = "Emil"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()