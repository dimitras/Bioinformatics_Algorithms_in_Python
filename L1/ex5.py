# Minimum Skew Problem: Find a position in a genome minimizing the skew.
# Input: A DNA string Genome.
# Output: All integer(s) i minimizing Skew(Prefixi (Text)) among all values of i (from 0 to |Genome|).

# python ex5.py ex5.txt

import sys

filename = sys.argv[1]

txt = open(filename)
seq = txt.readline().strip()

skew = 0
skews = []

for i in range(len(seq)):
	if seq[i] == 'C':
		skew -= 1
	elif seq[i] == 'G':
		skew += 1
	skews.append(skew)

min_skew = min(skews)
min_skews_positions = []
for i,value in enumerate(skews):
	if value == min_skew:
		min_skews_positions.append(str(i+1))

print " ".join(min_skews_positions)