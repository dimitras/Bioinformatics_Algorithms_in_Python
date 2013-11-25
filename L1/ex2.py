# Reverse Complement Problem: Reverse complement a nucleotide pattern.
# Input: A DNA string Pattern.
# Output: Pattern, the reverse complement of Pattern.
     
# python ex2.py dataset_3_2.txt

import sys

filename = sys.argv[1]

txt = open(filename)
seq = txt.readline().strip()

complements_dictionary = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
complement = ''
for n in seq:
	complement += complements_dictionary[n] 

reverse_complement = complement[::-1]

print reverse_complement