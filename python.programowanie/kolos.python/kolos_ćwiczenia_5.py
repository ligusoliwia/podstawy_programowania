#ZADANIE 15
class ZWIERZE:
    def __init__(self, imie: str, glos: str):
        if 3 <= len(imie) <= 20:
            self.imie = imie
        else:
            raise ValueError('spróbuj ponownie, imię zwierzaka powinno zawierać od 3 do 20 znaków')
        if 3 <= len(glos) <= 10:
            self.glos = glos
        else:
            raise ValueError('spróbuj ponownie, głos zwierzaka powinien zawierać od 3 do 10 znaków')
        
    def __str__(self):
        return f'imię twojego zwierzaka to {self.imie}, a głos to {self.glos}'
    
class PIES(ZWIERZE):
    def __init__(self, imie, glos = 'hau'):
        super().__init__(imie, glos)
    def przywolaj(self):
        print(self.glos)
        print('pies przyszedł, jak nie ugryzie to chyba cie lubi')
    
class KOT(ZWIERZE):
    def __init__(self, imie, glos = 'miau', i = 0):
        super().__init__(imie, glos)
        self.i = i
    def przywolaj(self):
        self.i += 1
        if self.i % len(self.imie) == 0:
            print(self.glos)
            print('kot przyszedł, jak nie podrapie to chyba cie lubi')

class CZLOWIEK(ZWIERZE):
    def __init__ (self, imie):
        super().__init__(imie, 'glos')
    def przywolaj(self, zwierze):
        print(f'{zwierze.imie}!')
        zwierze.przywolaj()

pies = PIES('creep', 'woof')
kot = KOT('weirdo', 'hiss')
czlowiek = CZLOWIEK('radiohead')

czlowiek.przywolaj(pies)
czlowiek.przywolaj(kot)
while kot.i % len(kot.imie) !=0:
    czlowiek.przywolaj(kot)


