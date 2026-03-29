def hamming(seq1, seq2):
    distance = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            distance += 1
    return distance

def res_record(file, distance, seq1, seq2):
    with open(file, "a") as res:
        res.write(f"para {seq1} i {seq2} ma odległość hamminga: {distance}" + "\n")

bugs = {1: "różna długość porównywanych sekwencji",
        2: "niezidentyfikowany znak",
        }

def bug_log(file, bug_type, seq1, seq2):
    bug_type = int(bug_type)
    with open(file, "a") as bug:
        bug.write(f"BŁĄD! para {seq1} i {seq2}, typ: {bugs[bug_type]}\n")

def ham_res(file, compare, altv):
    allowed = set("ACTG")
    with open(file, "r") as sq:
        sq = sq.readlines()
        seq = [line.strip().upper() for line in sq]

    if len(seq) % 2 != 0 and compare == 2:
        if altv == 1:
            compare = 1
            print("liczba sekwencji w pliku jest nieparzysta, zmiana trybu porównywania na 1")
        else: 
            quit()
            print("liczba sekwencji w pliku jest nieparzysta, następuje wyjście z programu.")

    if compare == 1:
        results = []
        #petla zew: wybiera 1 seq
        for i in range(len(seq)):
            #petla wew: wybiera kolejna seq
            for j in range(i + 1, len(seq)):
                s1 = seq[i]
                s2 = seq[j]

                #zgodnosc znakow
                if not (set(s1).issubset(allowed) and set(s2).issubset(allowed)):
                    bug_log("bug_logger_hamming.txt", 2, s1, s2)
                    continue

                if len(s1) == len(s2):
                    distance = hamming(s1, s2)
                    res_record("hamming_results.txt", distance, s1, s2)
                else:
                    bug_log("bug_logger_hamming.txt", 1, s1, s2)
                    print(f"wystąpił błąd, para {s1} i {s2}; patrz plik z błędami")
    
    if compare == 2:
        results = []
        for i in range(0, len(seq) - 1, 2): #range od zera do dlugosc pliku - 1, skok o 2
            s1, s2 = seq[i], seq[i+1] #dwie linie
            #sprawdzanie zgodnosci znakow
            if not (set(s1).issubset(allowed) and set(s2).issubset(allowed)):
                bug_log("bug_logger_hamming.txt", 2, s1, s2)
                continue

            if len(s1) == len(s2):
                distance = hamming(s1, s2)
                res_record("hamming_results.txt", distance, s1, s2)
            else:
                bug_log("bug_logger_hamming.txt", 1, s1, s2)
                print(f"wystąpił błąd, para {s1} i {s2}; patrz plik z błędami")
    



comp = input('''jakie porowananie sekwencji (podaj numer):
             1. każda z każdą,
             2. pierwsza z następną.
             wybór: ''')
c_type = int(comp)

alt = input('''w wypadku nieparzystej ilości sekwencji (podaj numer):
             1. zmień tryb porównania,
             2. zaznacz błąd i wyjdź z programu.
             wybór: ''')
a_type = int(alt)

if c_type not in [1, 2]:
    print("niepoprawny tryb, spróbuj ponownie :)")

if a_type not in [1, 2]:
    print("niepoprawny alternatywny tryb, spróbuj ponownie :)")

ham_res("testSEQ.txt", c_type, a_type)
