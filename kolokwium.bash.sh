#!/usr/bin/bash
# 2. Stwórz kod za pomocą, którego z liczb w zakresie 0-134 
#zostaną wyświetlone wszystkie liczby parzyste mniejsze od 70 
#oraz liczby nieparzyste większe od 40
echo "zadanie 2"
declare -a tab_z2
i=0
 while (( i<=134 )); do
    if (( i%2==0 && i<=70 )); then
        tab_z2+=("$i")
    elif (( i%2!=0 && i>=40 )); then
        tab_z2+=("$i")
    fi
((i++))
done
echo "${tab_z2[@]}"

# 5. Korzystając z pętli while napisz kod, który 
#wyświetli liczby od 17 do 4 z pominięciem liczb 11,9,3
echo "zadanie 5"
i=18
declare -a tab_z5
while (( i>=4 )); do
    ((i--))
    if (( i!=11 && i!=9 && i!=3)); then
    tab_z5+=("$i")
    else continue
    fi
done
echo "${tab_z5[@]}"

# 7. Stwórz skrypt obliczający sumę wartości minimalnej i maksymalnej tablicy.
echo "zadanie 7"
tab_z7=(1 3 2 4 6 5 8 9)
min=${tab_z7[0]}
max=${tab_z7[0]}
for i in "${tab_z7[@]}"; do
    if (( i<=min )); then
        min=$i
    fi
    if (( i>=max )); then
        max=$i
    fi
    ((i++))
done

sum=$((min + max))

echo "min wartość: $min"
echo "max wartość: $max"
echo "suma min i max = $sum"

# 8. Stwórz kod sortujący tablicę ustawiając wartości od największej do najmniejszej 
#co iterację wyświetl aktualny stan tablicy
echo "zadanie 8"
declare -a tab_z8=(1 3 2 4 6 5 8 9)
min=${tab_z8[0]}
max=${tab_z8[0]}
for i in "$tab_z8[@]"; do
    if (( i <= z=($i+1) )); then
    temp=${tab_z8[i]}
    tab_z8[0]=$i
    tab_z8[i]=$temp
    else 
    fi
    if (( i >= max )); then
    temp=(($tab_z8[0]))
    tab_z8[0]=$i
    tab_z8[i]=$temp
    fi
    ((i++))

