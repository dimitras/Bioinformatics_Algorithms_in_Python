# Pattern Matching Problem: Return all starting positions (in increasing order) where CTTGATCAT appears as a substring in the Vibrio cholerae genome.
# Input: Two strings, Pattern and Genome.
# Output: All starting positions where Pattern appears as a substring of Genome.
# Note: use 0-based indexing in problem implementations

# python ex3b.py ex3b_Vibrio_cholerae.txt

import sys

filename = sys.argv[1]

txt = open(filename)
pattern = txt.readline().strip()
seq = txt.readline().strip()

pattern_start_positions = []
for i in range(len(seq)-len(pattern)+1):
	if pattern == seq[i:i+len(pattern)]:
	    pattern_start_positions.insert(-1,str(i))

complements_dictionary = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

complement_pattern = ''
for n in pattern:
	complement_pattern += complements_dictionary[n] 

reverse_complement_pattern = complement_pattern[::-1]

# complement = ''
# for n in seq:
# 	complement += complements_dictionary[n] 

# reverse_complement = complement[::-1]

for i in range(len(seq)-len(pattern)+1):
	if reverse_complement_pattern == seq[i:i+len(pattern)]:
	    pattern_start_positions.insert(-1,str(i))


pattern_start_positions.sort()
print " ".join(pattern_start_positions)