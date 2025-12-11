#!/usr/bin/bash
i=0
j=0
echo "twoje poczatkowe zmienne to i=$i oraz j=$j"

while ! (( j>65 && i%2!=0 )); do #powtarzaj petle dopolki nie sa spelnione warunki
	i=$((i+1))
	
	if (( i%2==0 )); then
	j=$((j+3))
	echo "po iteracji $i twoje zmienne to: i=$i oraz j=$j"
	fi
done
echo "zostal spelniony warunek, koncowe wartosci to: i=$i a j=$j"
