#args & kwargs
#funkcja ma ustalona ilosc arg, ale jesli nie wiadomo ile ich bedzie?:

#czyli *args=tuple & **kwargs=dict

#ARBITARY ARGUMENT:
#przed argumentem *, np: def funkcja(*argument):
#zamiast jednego argumentu funkcja dostaje krotke
def arg(*radio):
    print(f"what the hell am i doin\' here! i\'m a {radio[1]}!")
#arg("nutjob", "creep", "weirdo")
#mozna z innymi argumentami
def arg(control, *radio):
    print(f"what the hell am i doin\' here! i\'m a {radio[1]} (i don\'t belong here! but you\'re so fckn {control}")
arg("special", "nutjob", "creep", "weirdo")

#ARBITARY KEYWORD ARGUMENT:
#przed argumentem **, np: def funkcja(**argument):
#tworzy slownik z argumentami
def smiths(**light):
    print(f"die by ur side {light["hev"]}")
smiths(hev = "is a heavenly way to die", eas = "the pleasure is mine!")