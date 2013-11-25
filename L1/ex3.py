# Pattern Matching Problem: Find all occurrences of a pattern in a string.
# Input: Two strings, Pattern and Genome.
# Output: All starting positions where Pattern appears as a substring of Genome.
# Note: use 0-based indexing in problem implementations

# python ex3.py ex3.txt

import sys

filename = sys.argv[1]

txt = open(filename)
pattern = txt.readline().strip()
seq = txt.readline().strip()

pattern_start_positions = []
for i in range(len(seq)-len(pattern)+1):
	if pattern == seq[i:i+len(pattern)]:
	    pattern_start_positions.insert(-1,str(i))

print " ".join(pattern_start_positions)