#!/bin/bash

if [ "$#" -gt 0 ]; then
    str1="https://en.wikipedia.org/wiki/"
    str2="$str1$1"
    echo $str2 >> $2
else
    echo -n "Enter search item: "
    read item
    echo -n "Enter logfile name: "
    read filename
    str3="https://en.wikipedia.org/wiki/"
    str4="$str3$item"
    echo $str4 >> $filename
fi
echo -ne '##### (33%)\r'
sleep 0.5
echo -ne '############# (66%)\r'
sleep 0.5
echo -ne '####################### (100%)\r'
echo -ne '\n'

