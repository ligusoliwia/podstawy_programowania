words = []
bleh = []

with open("fragmenty-A.txt", "r") as frag:
    for line in frag:
        cln = line.strip().split(";")
        for word in cln:
            word = word.strip()
            if len(word) == 9:
                words.append(word)
            else:
                bleh.append(word)


print(words)

with open("oliwia.ligus.txt", "w") as ol:
    ol.write(f"ilość wystąpień słów o długości 9: {len(words)}" + "\n")
    for w in words:
        ol.write(w + "\n")

print(f"ilość sekwencji nie spełniających warunku: {len(bleh)} :(")