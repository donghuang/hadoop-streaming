#!/usr/bin/env bash

while read LINE
do
  echo "$etldate 1"
  for word in $LINE
  do
    echo "$word 1"
  done
done

