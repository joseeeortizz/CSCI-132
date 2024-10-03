hi i am testing nano.

#!/bin/bash

# jose ortiz


# Function to display the usage message
usage() {
    echo "Usage: $0 <dna_file> <sequence1> [sequence2 ...]"
    exit 1
}

# Check if at least two arguments are provided
if [ $# -lt 2 ]; then
    echo "Error: Missing arguments."
    usage
fi

# Check if the first argument is a valid file
dna_file="$1"
if [ ! -f "$dna_file" ]; then
    echo "Error: DNA file '$dna_file' not found."
    usage
fi

# Read the DNA string from the file
dna_string=$(cat "$dna_file")

# Loop through the remaining arguments (sequences to search for)
shift  # Shift removes the first argument (dna_file)
for sequence in "$@"; do
    # Use grep to count the non-overlapping occurrences of the sequence
    count=$(echo "$dna_string" | grep -o "$sequence" | wc -l)
    # Output the sequence and its count
    echo "$sequence $count"
done