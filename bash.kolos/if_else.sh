#/!usr/bin/bash

#pętla if
#wykonuje instrukcję w zależności od warunku

#i=0 deklaracja odgórna zmiennej
read -p "podaj swój numer: " i #zapytanie użytkownika o wartość zmiennej
if (( i < 10 )); then 
    #postawienie warunku, jeśli jest prawdziwy wykona inst. po 'then' np.:
    echo "twój numer jest mniejszy od 10: > $i"
    else #określa alternatywę dla warunku
    #postawienie alternatywy:
    echo "twój numer jest większy od 10: < $i"
fi #kończy blok if
