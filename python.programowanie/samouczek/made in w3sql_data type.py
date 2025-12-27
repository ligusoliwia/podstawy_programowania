x = 'string'
y = 14.3
z = 3
a = True
print(type(x))
print(type(y))
print(type(z))
print(type(a))

conv = float(z)
print(type(conv))

unpacking = ('the', 'end', 'is', 'near')
a, b, c, d = unpacking
print(unpacking)
print(b)

import random
print(random.randrange(1,9)) #printuje random liczbe w range 1-9

chasing = 'pavements'
print(chasing[0])
#or print(chasing[2:4]) #range indexow 

up = 'i\'ll die on this hill' #slash pozwala na wpisanie w str cudzyslowia bez wypluwania bledu
print(up.upper())

down = 'NOTHING COULD MATTER'
print(down.lower())

spl = 'i wish, something could matter to you'
print(spl.split(","))

combo = up + ", " + down + ", " + spl
print(combo.lower())

mon = 9
txt = f'the price for ur soul is: {mon:.2f} monopoly money, good luck!'
print(txt)

import random
x = random.randrange(0,10)
y = random.randrange(0,10)
if x > y:
    print(True)
else:
    print(False)

print(f"{15%4}")
miau = 15%4
print(miau)
print(meow:=12%4)

nums = [1,2]
count = len(nums)
if count > 3:
    print(f'ur list is {count} lomng')
if (count := len(nums)):
    print(f'ur list is {count} lomng')

favsGA = ['tangerine', 'domestic bliss', 'ur love(deja vu)']
favsAM = ['no.1 party anthem', '505', 'certain romance']
fvGA = favsGA
print(favsGA is favsAM)
print(fvGA is favsGA)
print(favsAM is not favsGA)
print('tangerine' in favsGA)
print('505' not in favsAM)

tangerine = ["tastey"]
brain = ["got", "cuz", "i\'m"]
#brain[0] = [" "] #zamienia podane indexy
brain.append("braindead")
brain.insert(1, "nobody")
print(brain)
brain.extend(tangerine)
print(brain)
brain.sort()
print(brain)
numnom = [1, 2, 7, 1212, 55, 3, 23, 994, 1000 , 302, 203]
numnom.sort()
print(numnom)
numnom.sort(reverse = True)
print(numnom)
brain.reverse()
print(brain)

rah = {
    "artist": "deaftones",
    "genre": "alt rock",
    "track": "sextape"
}
print(rah["genre"])
print(len(rah))

