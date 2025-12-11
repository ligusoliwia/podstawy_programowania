#/!usr/bin/bash

#pętla for in
#przechodzi po wartościach/ liście których ilość jest nieznana/ duża
#pętla for in przechodzi po każdej wartości listy

for i in {1..150}; do
#jako zakres wartości można podać 'seq 0 5': przechodzi przez cyfry 0-5

#budowa pętli for in:
    #for <zmienna> in <lista/ zakres>; do
    echo $i #wyświetla wartości po każdej iteracji
    #między 'for in' a 'done' są polecenia do wykonania w tej pętli
done