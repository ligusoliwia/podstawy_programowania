#pętla która wyświetla wartości od 0 do 100
#pomija kolejne potegi dwojki 2^1 i tak dalej

#/!usr/bin/bash
i=0
p=0
declare -a tab(1..100)
    if (( i != 2^p )); then
        echo ${tab[i]}
        i=$((i+1))
        p=$((p+1))
    else
        continue
    fi
