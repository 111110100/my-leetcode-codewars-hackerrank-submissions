#!/bin/bash
time tr "\n" " " < words.txt |  tr -s " " "\n" | sort | uniq -c | sort -r | awk '{print $2,$1}'
echo
time cat words.txt | xargs -n1 | sort | uniq -c | sort -nr | awk '{print $2 " " $1}'
echo
time egrep -o [a-z]+ words.txt | sort | uniq -c | sort -nr | awk '{print $2,$1}'
