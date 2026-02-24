#/!usr/bin/bash

#pętla while
#powtarza kod dopółki nie zostanie spełniony określony warunek

declare -i i=0 #deklaracja zmiennej 'i'
while ((i<10)); do 
    #postawienie warunku, dopółki i < 10 kod będzie powtarzany
    echo $i #za każdą iteracją zmienna 'i' będzie wyświetlana
    ((i = i + 1)) #jeśli warunek pętli nie jest spełniony -> instrukcja
    #między 'while' a 'done' są polecenia do wykonania w tej pętli
done