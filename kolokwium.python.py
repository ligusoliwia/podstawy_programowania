#zadania: 3, 4, 6, 8, 9, 10
#ZADANIE 6(5p):
class SAMOCHOD:
    def __init__(self, marka, kolor, predkosc):
        if 3 <= len(marka) <= 20:
            self.marka = marka
        kolorki = ['czerwony', 'czarny', 'niebieski', 'szary']
        if kolor in kolorki:
            self.kolor = kolor
        if 0 <= predkosc <= 400:
            self.predkosc = predkosc
    def jedz():
        return 'zielone światło - auto jedzie!'
    def stoj():
        return 'czerwone światło - auto stoi!'
    def __str__(self):
        return f'pojazd {self.marka} w kolorze {self.kolor} o prędkości maksymalnej'
        



class ZWIERZE:
    def __init__(self, gatunek: str, masa: int):
        if 5<= len(gatunek) <= 40:
            self.gatunek = gatunek
        if masa > 0:
            self.masa = masa
    def zapoluj(self):

class TYGRYS(ZWIERZE):
    def __init__(self, gatunek = 'tygrys', masa):
        super().__int__(gatunek, masa)
class ZEBRA


#zadania: 5p, 5p, torche z 30p, 