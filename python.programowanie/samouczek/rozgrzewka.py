#Napisać program, który wczytuje od użytkownika kolejne liczby dopóki użytkownik nie poda słowa *stop*. 
#Następnie #program oblicza średnią tych liczb poprzez użycie funkcji `srednia` zdefiniowanej przez programistę.

def srednia(list) -> float:
    if len(list) == 0:
        return 0
    suma = 0
    for i in list:
        suma += i
    return suma / len(list)
    
numerki = []
while True:
    num = input("proszę ładnie o podanie numerków do średniej, lub 'stop' jeśli chcesz wyjść: ")
    if num.lower() == 'stop':
        break
    try:
        numerki.append(float(num))
    except ValueError:
        print('no chyba nie te znaki, próbuj dalej!')

if numerki:
    print(f'wow to twoja srednia {(srednia(numerki))}')
else:
    print('nie ma średniej - obawiam się że nie podałeś żadnych liczb!')

#Zmodyfikować program w taki sposób aby użytkownik mógł wprowadzić dowolnie wiele osób. 
#Kiedy skończy, program ma poprosić o podanie numeru użytkownika, którego użytkownik chce przedstawić. 
#Mechanizm wydobywania odpowiedniego użytkownika ma być zaimplementowany w funkcji, 
#która zwraca dane użytkownika do programu.