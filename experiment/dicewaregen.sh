#!/usr/bin/env bash

# generate 24 regular diceware passwords

count=0

while [ ${count} -lt 24 ]; do
    diceware --no-caps --num 2 -d .
    let count=count+1
done
