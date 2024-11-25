#!/bin/bash
# Usage : Assignment 7
# Author : Jose Ortiz
# Created on : November 25, 2024
# Description : atomcoordinates.sh is a bash script that reads a PDB file and extracts the atom serial number, X, Y, and Z coordinates of each atom in the file.
# The script uses awk to process the PDB file and extract the required information. The script takes a single argument, which is the path to the PDB file.
# The script checks if the argument is provided and if it is a readable file. If the argument is not provided or the file is not readable, the script displays an error message and exits. If the argument is provided and the file is readable, the script processes the PDB file using awk and extracts the atom serial number, X, Y, and Z coordinates of each atom in the file.
# The extracted information is displayed in a tabular format with the following columns: Atom serial number, X coordinates, Y coordinates, and Z coordinates. The script uses printf to format the output in a tabular format.
# The bash script is tested with different PDB files to ensure that it works correctly and displays the required information.
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

#*************************************************************