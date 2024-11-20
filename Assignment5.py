#!/bin/bash
# Usage : Assignment5
# Author : Jose Ortiz
# Created on : November 13, 2024
# Description : Assignment5.sh
#
#*************************************************************

# Check if a single argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <dna_file>"
  exit 1
fi

# Check if the argument is a file
if [[ ! -f "$1" ]]; then
  echo "$0: cannot open $1 for reading"
  exit 1
fi

# Read the DNA sequence from the file
dna=$(cat "$1")

# Check if the DNA sequence contains only 'a', 'c', 'g', and 't'
if [[ ! "$dna" =~ ^[acgt]+$ ]]; then
  echo "$0: invalid DNA sequence in $1"
  exit 1
fi

# Count codon occurrences
declare -A codon_counts

while [[ "$dna" != "" ]]; do
  codon="${dna:0:3}"
  dna="${dna:3}"
  ((codon_counts[$codon]++))
done

# Sort codons by frequency and alphabetical order
codon_counts_sorted=($(printf "%d %s\n" "${codon_counts[@]}" | sort -nr | cut -d " " -f 2-))

# Print the sorted codon counts
for codon in "${codon_counts_sorted[@]}"; do
  echo "${codon_counts[$codon]} $codon"
done