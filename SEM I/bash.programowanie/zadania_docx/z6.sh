#zmienna iteruje sie od 0 do 100
#break kiedy zmienna^2 > 100

#!/bin/bash
num=0
while (( i**2 <= 100 )); do
    if (( i**2 < 100 )); then
        ((i++))
        echo $i
    else
        ((i++))
        echo "kwadrat $i przekracza wartość 100"
        break
    fi
done