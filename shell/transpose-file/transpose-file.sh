#!/bin/bash
time cat file.txt | awk '{for(i=0;++i<=NF;)a[i]=a[i]?a[i] FS $i:$i}END{for(i=0;i++<NF;)print a[i]}'
echo
time awk '{for(i=0;++i<=NF;)a[i]=a[i]?a[i] FS $i:$i}END{for(i=0;i++<NF;)print a[i]}' file.txt
echo
time awk 'NR == 1 {for (i = 1; i <= NF; i++) {cols[i] = $i}} NR > 1 {for(i = 1; i <= NF; i++) {cols[i] = cols[i]" "$i}} END {for (k in cols) {print cols[k]}}' file.txt
echo
ncol=`head -n1 file.txt | wc -w`

for i in `seq 1 $ncol`
do
    echo `cut -d' ' -f$i file.txt`
done
