#!/bin/bash
# Usage : Assignment 7
# Author : Jose Ortiz
# Created on : November 20, 2024
# Description : atomcoordinates.sh
#
#*************************************************************


 
#!/bin/bash

# Function to display usage message
usage() {
    echo "Usage: $0 <PDB file>"
    exit 1
}

# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
    echo "Error: Expected one argument."
    usage
fi

# Check if the argument is a readable file
if [ ! -f "$1" ] || [ ! -r "$1" ]; then
    echo "Error: '$1' is not a readable file."
    usage
fi

# Process the PDB file
awk '
    BEGIN {
        printf "%-25s%-20s%-20s%-20s\n", "Atom serial number:", "X coordinates:", "Y coordinates:", "Z coordinates:"
    }
    /^ATOM/ {
        serial_number = substr($0, 7, 5)
        x_coord = substr($0, 31, 8)
        y_coord = substr($0, 39, 8)
        z_coord = substr($0, 47, 8)
        printf "%-25s%-20s%-20s%-20s\n", serial_number, x_coord, y_coord, z_coord
    }
' "$1"