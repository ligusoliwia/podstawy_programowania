indexy = open("indexy.txt")
ind = {}
inne_ind = {}
for linia in indexy:
    line_split = linia.split()
    n=0
    ind[line_split[0]] = [line_split[1], line_split[2]]
    #kluczem ma być połączenie dwóch kluczy (bez przerwy)
    inne_ind[line_split[1]+line_split[2]] = line_split[0]

print(ind)