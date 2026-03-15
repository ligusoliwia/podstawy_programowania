#ZADANIE 1
historia = []
class KONTO:
    def __init__(self, wlasc: str, p_stan = 0):
        self.wlasc = wlasc
        self.p_stan = p_stan
        self._historia = [f'otwarcie konta: {p_stan} PLN']
    def wplac(self, kwota):
        self.p_stan += kwota
        self._historia.append(f'wpłata: {kwota}')
        return f'wpłacono {kwota}, nowy stan konta: {self.p_stan}'
    def wyplac(self, kwota):
        if kwota <= self.p_stan:
            self.p_stan -= kwota
            self._historia.append(f'wypłata {kwota}')
            return f'wypłacono {kwota}, nowy stan konta {self.p_stan}'
        else:
            print('przykro mi, ale nie posiadasz wystarczających środków na koncie')
            return 'brak środków'
    @property
    def historia(self):
        return self._historia
    def __str__(self):
        return f'konto użytkownika {self.wlasc} aktualnie posiada {self.p_stan} PLN'

k = KONTO("blachaj", 100)
k.wplac(50)
k.wyplac(30)
print(k)
print(k.historia)


#ZADANIE 3
class PROSTOKAT:
    def __init__(self, a, b):
        if a > 0 and b > 0:
            self.a = a
            self.b = b
        else:
            print('niepoprawne wartosci')
    def pole(self):
        return self.a*self.b
    def obwod(self):
        return 2*self.a + 2*self.b
    def kwd(self):
        if self.a == self.b:
            return True
        else:
            return False
    def skaluj(self, mnoznik):
        if mnoznik > 0:
            self.a *= mnoznik
            self.b *= mnoznik
            return f'nowe boki to {self.a} i {self.b}'
        else:
            return 'mnożnik musi być dodatni'

p = PROSTOKAT(3, 8)
print(f'pole {p.pole()}')
print(f'obwód: {p.obwod()}')
p.skaluj(4)
print(f'pole po skalowaniu: {p.pole()}')

#ZADANIE 4
class ROBOT:
    def __init__(self, model: str, bateria: int):
        self.model = model
        self.bateria = bateria
    def pracuj(self):
        raise NotImplemented('klasa musi implementować tą metodę')
class ROBOT_SP(ROBOT):
    def pracuj(self):
        if self.bateria >= 10:
            self.bateria -= 10
            return 'odkurzam...'
        else:
            return 'bateria rozładowana'
class ROBOT_KUCH(ROBOT):
    def __init__(self, model: str, bateria: int, tryb: str):
        super().__init__(model, bateria)
        tryby = ['siekanie', 'mieszanie', 'smażenie', 'pieczenie']
        if tryb in tryby:
            self.tryb = tryb
        else:
            raise ValueError(f'nie ma takiego trybu, wybierz: {tryby}')
    def pracuj(self):
        return f'{self.model} wykonuje {self.tryb}'
class OPERATOR:
    def uruchom_maszyne(self, robot: ROBOT):
        print(f'operator uruchamia robota: {robot.model}')
        print(robot.pracuj())

r_odkurzacz = ROBOT_SP('bakoma', 3)
r_mikser = ROBOT_KUCH('twist', 15, 'pieczenie')
op = OPERATOR()
op.uruchom_maszyne(r_odkurzacz)
op.uruchom_maszyne(r_mikser)
op.uruchom_maszyne(r_mikser)