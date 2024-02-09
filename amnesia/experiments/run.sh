#!/bin/bash

S='0'
for i in $(seq 1 1 1000)
do 
    S=$(echo $S | exec "./increment")
done