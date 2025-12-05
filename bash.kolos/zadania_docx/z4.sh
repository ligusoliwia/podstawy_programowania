#kod pętli która iteruje od 0 do 100:
#wyświetla tylko parzyste liczby < 20
#i nieparzyste liczby > 80

#/!bin/bash

i=0
declare -a tab_par
declare -a tab_npar

while ((i<=100)); do    
    if ((i%2==0 && i<20)) then
        tab_par+=("$i")
    fi

    if ((i%2!=0 && i>80)) then
        tab_npar+=("$i")
    fi
    i=$((i+1))
done
echo "liczby parzyste mniejsze od 20 to: ${tab_par[@]}, 
liczby nieparzyste większe od 80 to: ${tab_npar[@]}"