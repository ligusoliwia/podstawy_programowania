#zmienna iteruje sie od 0 do 10, nie wyświetla 2, 3, 7  
#koncy dzialanie kiedy zmienna == 9

#!/bin/bash
i=0
while (( i <= 9 )); do
    if (( i != 2 || i != 3 || i != 7 )); then
        echo $i
        ((i++))
    fi
done
