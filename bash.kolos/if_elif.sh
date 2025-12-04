#/!usr/bin/bash

#pętla if
#wykonuje instrukcję w zależności od warunku

#i=0 deklaracja odgórna zmiennej
read -p "podaj swój numer: " i #zapytanie użytkownika o wartość zmiennej
if (( i < 100 )); then #postawienie warunku, jeśli jest prawdziwy wykona inst. po 'then' np.:
    echo "twój numer jest mniejszy od 100: > $i"
    elif (( i < 200 )); then #określa 1 alternatywę dla warunku, trzeba podać nowy warunek
        echo "twój numer jest mniejszy od 200: > $i"
    elif (( i < 300)); then #określa kolejną alternatywę dla wcześniejszego warunku
        echo "twój numer jest mniejszy od 300: > $i"
    else
        echo "twój numer jest większy od 300: < $i"
    #else dyktuje końcowy warunek, jeśli zmienna nie spełniła żadnego poprzedniego
fi #kończy blok if
