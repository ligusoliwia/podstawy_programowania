#zadeklarować tablicę: 1-7
#kod ma zamienić miejscami 3 pierwsze i ostatnie elementy

#/!bin/bash

declare -a tab_7=(1 2 3 4 5 6 7)
temp=$((tab_7[0]))
tab_7[0]=$((tab_7[6]))
tab_7[6]=$temp

temp=$((tab_7[1]))
tab_7[1]=$((tab_7[5]))
tab_7[5]=$temp

temp=$((tab_7[2]))
tab_7[2]=$((tab_7[4]))
tab_7[4]=$temp

echo "${tab_7[@]}"
