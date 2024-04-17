#!/bin/bash

S='0'
for ((i = 1; i <= 300; i++)); do
    if ((i % 100 == 0)); then
        echo $i
    fi
    S=$(echo $S | ./increment)
done
echo $S