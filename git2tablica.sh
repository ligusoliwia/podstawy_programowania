#/!usr/bin/bash
#deklaracja tablicy
declare -a tab=(100 12 9 70 16 0 81)
tab+=("15")
tab+=("49")
tab+=("99")
#zamiana elementow msc i wyswietlenie tablicy
temp=${tab[0]}
tab[0]=${tab[1]}
tab[1]=$temp
echo "${tab[@]}"
#szukanie minimum tablicy
min=${tab[0]}
for i in "${tab[@]}"; do
	if ((i < min)); then
	min=$i
	fi
done
echo "minimum tablicy to $min"

