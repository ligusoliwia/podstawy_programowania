#napisz kod pętli, która w iteracjach od 0 do 1000 wyświetli:
#wszystkie liczby podzielne przez 100

#/!bin/bash

i=0
while ((i<=1000)); do
    i=$((i+1))
    
    if (( i%100==0 )); then
    echo $i
    else continue
    fi

 done