#!/usr/bin/bash
a=2
b=4
c=7
i=0

while (( $i < 20 )); do
	i=$((i + 1))
	a=$((a * i))
	b=$((b + a + i))
	c=$((c + a - $i))
echo "iteracja $i: a=$a, b=$b, c=$c"

	if (( $a%2==0 && $b%2==0 && $c%2==0 )); then
	echo "liczby sa parzyste -> koniec petli!"
	break
	fi
done
