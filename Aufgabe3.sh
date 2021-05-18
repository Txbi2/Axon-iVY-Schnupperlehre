name=`dialog --inputbox "Wie heißen Sie?" 0 0 "" \
 3>&1 1>&2 2>&3`
alter=`dialog --inputbox "Wie alt sind Sie?" 0 0 "" \
 3>&1 1>&2 2>&3`
Wohnort=`dialog --inputbox "Wo Wohnen Sie?" 0 0 "" \
 3>&1 1>&2 2>&3`
dialog --msgbox "Hallo $name, du bist $alter Jahre Alt und wohnst in $Wohnort" 5 70