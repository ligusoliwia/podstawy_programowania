#zadeklaruj 2 tablice o takim samym rozmiarze
#obliczyc sume tych samych indexow
    #wynik do 3 tablicy


#!/usr/bin/bash

declare -a tab1=(1 2 3 4 5 6 7 8 9 10)
declare -a tab2=(11 22 33 44 55 66 77 88 99 100)
declare -a tab3
i=0

for ((i = 0; i <= 9; i++)); do
tab3[i]=$((tab1[i]+tab2[i]))
done
echo "${tab3[@]}"

