def steviewonder(): #definicja funkcji o danej nazwie():
    print('''lately i had the strangest feeling
          and i\'m a man of many wishes,
          please don\'t make me cry,
          cause this time it\'s truly goodbye''') #cokolwiek co funkcja ma wykonywać
    return True #zwraca do kodu wartosc, ale nie wyswietla - zapisuje
steviewonder() #wywołanie funkcji
message = steviewonder()
print(message) #zeby wyswietlic zreturnawna watosc

def passing_through():
    pass #tworzy 'placeholder', funkcjie nie moga byc puste

def sinatra(track): #w nawiasach arumenty po przecinkach
    print(track, "simply lovely") 

sinatra("strangers in the night") #potem przy wywolaniu funkcji wypelnia sie argument (jesli dynamiczny)
#eg
def forever_young(age = 25): #mozna ustalic default argument
    if age <= 25:
        print(f"oh my dear, only {age}, shall we be forever young, maybe not?")
    else:
        print(f"lost your youth, but still only {age}, many beauties of life before you")
forever_young(18)
forever_young(32) #ilosc arg wywolanych = wpisanych
forever_young() #default arg

def clear(name = "crystal", state = "significant"):
    usr = input("mind telling me who's this mysterious shadow? or pass: ")
    if usr == "pass":
        return f"that\'s what u end up with punk: {name} is {state}"
    else:
        usr_id = input("well, just how important is that special someone? or pass: ")
        return f"youre soso sweet {usr}, very {usr_id}"
#print(clear())

def over(world):
    for i in world:
        print(i)
worlds = ["the", "world", "we", "knew", "over", "and", "over", "again"]
#over(worlds)