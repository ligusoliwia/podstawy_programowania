#/!usr/bin/bash

#pętla for
#przechodzi po wartościach których ilość jest znana

for ((i = 0; i < 10; i++)); do
#budowa pętli for:
    #for ((zmienna; warunek kończący pętlę; instrukcja: +/- zmienna)); do
    #np.: ((i = 0; i < n; i++)) == ((i = 0; i < n; i = i + 1))
    echo $i #wyświetla zmienną po każdej iteracji
    #między 'for' a 'done' są polecenia do wykonania w tej pętli
done