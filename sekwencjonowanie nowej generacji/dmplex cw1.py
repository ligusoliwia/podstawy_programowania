indexy = {
    ("ACTG", "GTCA"): "S1.txt",
    ("CTGA", "AGTC"): "S2.txt"
} #charakterystyczny początek i koniec dla danej próbki

with open("sekwencje.txt", "r") as seq, open("undetermined.txt", "w") as idk:
#with open pozwala na brak manualnego zamknięcia pliku (brak leakow np)
    for linia in seq:
        sekwencja = linia.strip() #odczyt lini (strip usowa spacje)
        
        #wycięcie początkowych i końcowych znaków
        start = sekwencja[:4]
        end = sekwencja[-4:]
        id = (start, end)

        #sprawdzenie czy para (start, end) jest indexem sekwencji
        if id in indexy:
            jakis_plik = indexy[id]
            #zapisujemy do właściwego pliku (tryb 'a' - dopisz)
            with open(jakis_plik, "a") as seq_res:
                seq_res.write(sekwencja + "\n")
        else:
            #jeśli nie pasuje, trafia do "undetermined"
            idk.write(sekwencja + "\n")

#"r" - tylko odczyt
#"w" - zapis (nadpisanie treści)
#"a" - dopisanie do końca pliku (append)