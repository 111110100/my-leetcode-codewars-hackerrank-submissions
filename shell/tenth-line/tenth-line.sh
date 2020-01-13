#!/bin/bash
time head -10 file.txt | awk 'END { print (NR < 10) ? "" : $0 }'
echo
time tail -n +10 file.txt | head -n 1
echo
time sed -n 10p file.txt
echo
time awk "NR==10" file.txt

