#pętla która wyświetla wartości od 0 do 100
#pomija kolejne potegi dwojki 

#!/usr/bin/bash
i=0
p=0
while (( i <= 100 )); do
    if (( i != 2**p )); then
        echo $i
        ((i=i+1))
    else
        ((i=i+1))
        ((p=p+1))
        continue
    fi
done
