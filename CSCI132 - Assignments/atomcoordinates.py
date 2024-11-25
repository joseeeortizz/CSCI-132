# Assignment 7
# Usage : python3 atomcoordinates.py
# Author : Jose Ortiz
# Created on : November 22, 2024.
# Description :
#
#*************************************************************

#!/usr/bin/env python3

import sys
import os

def usage():
    print("Usage: python3 atomcoordinates.py <PDB file>")
    sys.exit(1)

# Check the number of arguments
if len(sys.argv) != 2:
    print("Error: Expected one argument.")
    usage()

# Check if the file exists and is readable
file_path = sys.argv[1]
if not os.path.isfile(file_path) or not os.access(file_path, os.R_OK):
    print(f"Error: '{file_path}' is not a readable file.")
    usage()

# Process the PDB file
try:
    print(f"{'Atom serial number:':<25}{'X coordinates:':<20}{'Y coordinates:':<20}{'Z coordinates:':<20}")
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("ATOM"):
                serial_number = line[6:11].strip()
                x_coord = line[30:38].strip()
                y_coord = line[38:46].strip()
                z_coord = line[46:54].strip()
                print(f"{serial_number:<25}{x_coord:<20}{y_coord:<20}{z_coord:<20}")
except Exception as e:
    print(f"Error while processing file: {e}")
    sys.exit(1)