# Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
# Input: Two strings Pattern and Text along with an integer d.
# Output: All positions where Pattern appears in Text with at most d mismatches.

# python ex6.py ex6.txt

import sys

filename = sys.argv[1]

txt = open(filename)
pattern = txt.readline().strip()
seq = txt.readline().strip()
max_mismatches = int(txt.readline().strip())

pattern_pos = []
for i in range(len(seq) - len(pattern) + 1):
    kmer = seq[i:i+len(pattern)]
    mismatches = 0
    for j, n in enumerate(kmer):
		if (n != pattern[j]):
			mismatches += 1
    if mismatches <= max_mismatches:
    	pattern_pos.append(str(i))

print " ".join(pattern_pos)
