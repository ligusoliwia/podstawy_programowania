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
        results[sample] = [] #'sample_id:" "jakas sekwencja", tworzy liste dla nazw sampli w dict

    with open(seq_plik, "r") as seq:
        for line in seq:
            line = line.strip()
            if not line:
                continue
            #snipsnip indeksy (8 od początku i od końca)
                #UWAGA na ilosc barcodow bo nic nie znajdzie jak zle wpisane
            i1 = line[:8] #poczatkowy barcode
            i2 = line[-8:] #koncowy barcode
            key = f"{i1}+{i2}"
            
            #czy i1+i2 sekwencji pasuja do jakiegos sampla z dict??
            sample_id = indexy.get(key, "bleh")
            
            #przypisanie sekwencji do sampla
            results[sample_id].append(line)
            
    return results

import csv
def save_final(results, file):
    with open(file, mode='w', newline='') as output:
        writer = csv.writer(output)
        
        #kolumny nnazwy
        writer.writerow(["Sample_ID", "Sequence"])
        #przepisanie ze slownika wynikow
        for sample_id, sequences in results.items():
            for seq in sequences:
                writer.writerow([sample_id, seq])


index = read_id("indexy.txt")
sorted_results = dmplex("sekwencje.txt", index)
save_final(sorted_results, "omg.csv")

