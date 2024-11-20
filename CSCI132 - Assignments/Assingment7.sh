#!/bin/bash
# Usage : Assignment7
# Author : Jose Ortiz
# Created on : November 20, 2024
# Description : Assignment7.sh
#
#*************************************************************
#!/bin/bash

# Check if a single argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <pdb_file>"
  exit 1
fi

# Check if the argument is a file
if [[ ! -f "$1" ]]; then
  echo "$0: cannot open $1 for reading"
  exit 1
fi

# Extract ATOM records and print coordinates
while read line; do
  if [[ "$line" =~ ^ATOM ]]; then
    serial=$(echo "$line" | cut -c 7-11)
    x=$(echo "$line" | cut -c 31-38)
    y=$(echo "$line" | cut -c 39-46)
    z=$(echo "$line" | cut -c 47-54)
    echo "Atom serial number: $serial"
    echo "X coordinates: $x"
    echo "Y coordinates: $y"
    echo "Z coordinates: $z"
    echo
  fi
done < "$1"
