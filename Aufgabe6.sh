genratedNumber=$((RANDOM % 100))
echo $genratedNumber
read -p "Gib eine Zahl ein:" zahl
while [ "$genratedNumber" -ne "$zahl" ]
do
    i=$((i+1))
    if (("$genratedNumber" < "$zahl"))
    then
        read -p "Gib eine kleinere Zahl ein:" zahl
    else
        read -p "Gib eine grössere Zahl ein:" zahl
    fi
done 
    echo "Du Hast die Zahl erraten "

    echo "Du hast $i versuche gebraucht"