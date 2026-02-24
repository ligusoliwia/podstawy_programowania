#modyfikacja zadania 3:
#kod ma nie wyświetlać 400, 500, 800
    #napisz kod pętli, która w iteracjach od 0 do 1000 wyświetli:
    #wszystkie liczby podzielne przez 100

#/!bin/bash

i=0
declare -a tab
while ((i<=1000)); do
    i=$((i+1))
        if (( i%100==0 && i!=400 && i!=500 && i!=800)); then
        tab+=("$i")
        else continue
        fi
 done
 echo "${tab[@]}"