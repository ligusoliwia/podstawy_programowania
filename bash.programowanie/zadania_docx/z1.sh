#napisz kod pętli, która przy każdym kroku zwiększa wartość: 
#zmiennej x o 2
#zmiennej y o 3
#zmiennej z o sumę y i z
#max. 10 kroków i wszystkie zmienne parzyste

#!/bash/bin
read -p "podaj wartość dla x: " x
read -p "podaj wartość dla y: " y
read -p "poadj wartość dla z: " z
#usr podaje własne zmienne

i=0 #'licznik' operacji
while ((i <= 10)); do #pętla wykonywana do osiągnięcia danego warunku
    x=$((x + 2)) #zapis obliczeń arytmetycznych do nowej zmiennej
    y=$((y + 3)) #zapis 'y=y+3' to zapis tekstowy
    suma=$((y + x)) #zapis tekstowy nie jest odbierany jako obliczenie!
    z=$((z + suma))
    ((i=i+1))

        if (( x % 2 == 0 && y % 2 == 0 && z % 2 == 0 )); then
            break
            else continue
        fi
        #po każdym kroku z while blok if sprawdza czy
        ##zostały spełnione pozostałe wymagania
done
echo "twoje końcowe wartości to x=$x, y=$y oraz z=$z, algorytm został
    zakończony po $i krokach"