#pętla while:
#msc tablicy zamiana: pierwsze ostatnie etc

#/!bin/bash
declare -a tab_8=(1 2 3 4 5 6 7 8 9 10)

i=0
z=$((${#tab_8[@]} - 1)) #-1 bo indexy są od 0
echo "twoja początkowa tablica: ${tab_8[@]}"
while (( i < z )); do
    temp=$((tab_8[$i]))
    tab_8[$i]=$((tab_8[$z]))
    tab_8[$z]=$temp
i=$((i+1))
z=$((z-1))
done
echo "twoja koncowa tablica: ${tab_8[@]}"