#!/bin/bash

if [ "$#" -ne 4 ]
then
    echo "$0 <Hight> <Weight> <fill or not (0\1)> <Char>"
    exit 1
fi

Hight=$1
Weight=$2

if [ $3 -eq 0 ]
then
    Fill_Char=' '
else
    Fill_Char=$4
fi

for (( i = 1; i <= $Hight; i++ )); do
  for (( j = 1; j <= $Weight; j++ )); do
    if (( 1 == i || $Hight == i || 1 == j || $Weight == j )); then
      echo -n $4
    else
      echo -n "$Fill_Char"
    fi
  done
  echo
done