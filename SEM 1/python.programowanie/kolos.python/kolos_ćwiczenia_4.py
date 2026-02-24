#ZADANIE 11
class SAMOCHOD:
    def __init__(self, marka: str, kolor: str, moc: float):
        if 3 <= len(marka) <= 20:
            self.marka = marka
        else:
            raise ValueError('spróbuj ponownie, marka powinna mieć od 3 do 20 znaków!')
        a_kolory = ['czerwony', 'czarny', 'niebieski', 'szary']
        if kolor.lower() in a_kolory:
            self.kolor = kolor
        else:
            raise ValueError(f'spróbuj ponownie, dozwolone kolory to: {a_kolory}.')
        if 0 <= moc <= 1000:
            self.moc = moc
        else:
            raise ValueError('spróbuj ponownie, maksymalna moc to 1000.')
    
    def jedz(self):
        if not self.ruch:
            self.ruch = True
            print('zielone światło! samochód wystartował.')
        else:
            print('samochód przemieszcza się.')
    
    def stoj(self):
        if self.ruch:
            self.ruch = False
            print('czerwone światło! samochód się zatrzymał.')
        else:
            print('samochód stoi.')

    def __str__(self):
        return f'pojazd {self.marka} w kolorze {self.kolor} o mocy maksymalnej {self.moc} KM'
    
autko = SAMOCHOD('porsche', 'czarny', 1000)
print(autko)
autko.ruch = False
autko.jedz()
print(autko.ruch)
autko.stoj()
print(autko.ruch)

#ZADANIE 12
class LICZNIK:
    def __init__(self, licznik_start = 0):
        self.licznik_start = licznik_start
        self.aktualny = licznik_start
    def inkrementuj(self):
        self.aktualny += 1
        return self.aktualny
    def dekrementuj(self):
        self.aktualny -= 1
        return self.aktualny
    def resetuj(self):
        self.aktualny = self.licznik_start
        return self.aktualny
    @property
    def wartosc(self):
        return self._aktualny


licz = LICZNIK()
print(licz.inkrementuj())
print(licz.dekrementuj())
print(licz.resetuj())

#ZADANIE 13
class PUNKT:
    def __init__(self, x, y) -> float:
        self.x = x
        self.y = y
    def przesun(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f'''punkt został przesunięty o wartości : {dx}, {dy}, 
              aktualne położenie punktu to x: {self.x} oraz y: {self.y}''')
    def odleglosc(self, nowy):
        odleglosc_x = abs(self.x - nowy.x)
        odleglosc_y = abs(self.y - nowy.y)
        return f'odległość nowego punktu od x ({self.x}): {odleglosc_x}, od y ({self.y}): {odleglosc_y}'
    
p1 = PUNKT(2,10)
p2 = PUNKT(8,3)
print(p1.odleglosc(p2))

#ZADANIE 14
class TEMPERATURA:
    def __init__(self, temp_k: float):
        if temp_k > 0:
            self.temp_k = temp_k
            print(f'twoja temperatura w stopniach kelvina to: {self.temp_k}')
        else:
            raise ValueError('przykro mi, ale temperatura nie może być zerem absolutnym')
        
    @property
    def cel(self):
        return self.temp_k - 273.15 #zmiana wartości na celcjusz
    @cel.setter
    def cel(self, temp_c):
        temp_k_nowa = temp_c + 273.15 #zmiana z powrotem na kelviny
        if temp_k_nowa < 0:
            raise ValueError('przykro mi, ale temperatura nie może być zerem absolutnym')
        else:
            self._temp_k = temp_k_nowa #aktualizuje temerature kelv
            print(f"zaktualizowana temperatura w kelvinach to: {self._temp_k:.3f}")
    
    @property
    def far(self):
        return (self.temp_k - 273.15) * 9/5 + 32 #konwertuje na celcjusza potem fahrenheita
    @far.setter
    def far(self, temp_f):
        temp_k_nowa = (temp_f - 32) * 9/5 + 273.15
        if temp_k_nowa < 0:
            raise ValueError('przykro mi, ale temperatura nie może być zerem absolutnym')
        else:
            self._temp_k = temp_k_nowa
            print(f"zaktualizowana temperatura kelvina to: {self._temp_k:.3f}")
    
    def __str__(self):
        return f'''podsumowywując! oto twoja wpisana temperatura (K): {self.temp_k}
        oto twoja temperatura w skali Celcjusza: {self.cel:.3f}
        oto twoja temperatura w skali Fahrenheita: {self.far:.3f}'''

test = TEMPERATURA(435)
print(test)
test.cel = 20
test.far = 10


    



