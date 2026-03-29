seq1 = "ACTGGT" #["A", "C", "T", "G", "G", "T"]
seq2 = "AATGCA" #["A", "A", "T", "G", "C", "A"]

hamming = []
for i in range(len(seq1)):
    if len(seq1) == len(seq2):
        if seq1[i] == seq2[i]:
            hamming.append(0)
        else:
            hamming.append(1)
    else:
        break

if hamming:
    odleglosc = sum(hamming)
    print(odleglosc)
else:
    print("podane seq sa roznych dlugosci!")