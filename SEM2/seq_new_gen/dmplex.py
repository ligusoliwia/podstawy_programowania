#czytanie indexow i slownik
def read_id(indexy_plik):
    index_dict = {}

    with open(indexy_plik, "r") as inx:
        for line in inx:
            separated = line.strip().split("\t") #dzieli po tabulatorze
            if len(separated) >= 3: #sample_id, start, stop
                sample_name = separated[0].strip() #nazwa probki
                index_1 = separated[1].strip() #index poczatkowy (i1)
                index_2 = separated[2].strip() #index koncowy (i2)
                inx = f"{index_1}+{index_2}"
                index_dict[inx] = sample_name #format zapisania indexow
                               
    return index_dict

#sprawdzanie indexow z seqwncjami
def dmplex(seq_plik, indexy):
    #nazwa_probki -> lista pełnych sekwencji
    results = {}
    
    results["bleh"] = [] #na sekwencje niedopasowane

    #listy dla kazdej probki
    for sample in indexy.values():
        results[sample] = [] #'sample_id:" "jakas sekwencja", tworzy liste od nazw sampli w dict

    with open(seq_plik, "r") as seq:
        for line in seq:
            line = line.strip()

            #snipsnip indeksy (8 od początku i od końca)
            i1 = line[:8] #poczatkowy barcode
            i2 = line[-8:] #koncowy barcode
            key = f"{i1}+{i2}"
            
            #czy i1+i2 sekwencji pasuja do jakiegos sampla z dict??
            sample_id = indexy.get(key, "bleh")
                #.get() → jesli znajdzie index to dodaje do listy danego sampla, jesli nie (alt) dodaje to bleh
            
            #przypisanie sekwencji do sampla
            results[sample_id].append(line)
            
    return results

#ZAPISAC DO PLIKU Z WRITE
#def save(res, out_plik):
#    with open(out_plik, "w", newline="") as res_csv:

def save_file(file, results):
    with open(file, "w", newline="") as f:
        for line in results:
            f.write(line + "\n")

def save_file(file, results):
    with open(file, "w", newline="") as f:
        for sample_id, sequences in results.items():
            for seq in sequences:
                f.write(f"{sample_id}\t{seq}\n")

index = read_id("indexy.txt")
sorted_results = dmplex("sekwencje.txt", index)
print(sorted_results)
save_file("final_seq.txt", sorted_results)

