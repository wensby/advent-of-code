#!/bin/bash

if [ $# -eq 0 ] ; then
  echo "No arguments supplied"
fi

name=$1
input=$2
output=$3

echo $input > ${name}.input
echo $output > ${name}.output
