#!/bin/Bash
# Author: Juan Pablo Nahuelpán
filename=$1
a=()

while IFS= read -r line; do
    a=(${a[@]} $line)
done < "$filename"

N="${#a[@]}"
count=0
for ((i=0; i<N; i++)); do
    for ((j=i+1; j<N; j++)); do
        for ((k=j+1; k<N; k++)); do
            if [ $((${a[$i]} + ${a[$j]} + ${a[$k]})) -eq 0 ]; then
                let count++
                echo $count 
            fi
        done
    done
done
# 1 year.
echo $count