#args & kwargs
#funkcja ma ustalona ilosc argumentów, ale co jesli nie wiadomo ile ich bedzie?:
#czyli *args = tuple & **kwargs = dict

#ARBITARY ARGUMENT (*arg):
#przed argumentem *, np: def funkcja(*argument):
#zamiast jednego argumentu funkcja dostaje krotke (tuple)

#def arg(*radio):
    #print(f"what the hell am i doin\' here! i\'m a {radio[1]}!") #do argumentu odwołuje się jak do zwykłej krotki np. nazwa[index]
#arg("nutjob", "creep", "weirdo")

#mozna dodać inne argumenty:
def arg(control, *radio):
    print(f"what the hell am i doin\' here! i\'m a {radio[1]} (i don\'t belong here! cuz i\'m a {radio[2]}) but you\'re so {control}")
arg( "special", "nutjob", "creep", "weirdo")


#ARBITARY KEYWORD ARGUMENT:
#przed argumentem **, np: def funkcja(**argument):
#tworzy slownik z argumentami
def smiths(**light):
    print(f"die by ur side {light["hev"]}, and so {light["eas"]}")
smiths(hev = "is a heavenly way to die", eas = "the pleasure is mine!")