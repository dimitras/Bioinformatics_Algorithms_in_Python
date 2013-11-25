# Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string
# Input: A string Text as well as integers k and d (You may assume k < 12 and d < 3)
# Output: All most frequent k-mers with up to d mismatches in Text

# python ex7.py ex7.txt

import sys

filename = sys.argv[1]

txt = open(filename)
(seq,max_kmer_length,max_mismatches) = txt.readline().strip().split(' ')

kmer_counts = {}
for i in range(len(seq)-int(max_kmer_length)+1):
	kmer = seq[i:i+int(max_kmer_length)]
	if kmer not in kmer_counts:
		pattern_pos = []
		for k in range(len(seq) - len(kmer) + 1):
		    pattern = seq[k:k+len(kmer)]
		    mismatches = 0
		    for j, n in enumerate(pattern):
				if (n != kmer[j]):
					mismatches += 1
		    if mismatches <= int(max_mismatches):
		    	pattern_pos.append(k)
		kmer_counts[kmer] = len(pattern_pos)

max_count = max(kmer_counts.values())

most_frequent_kmers = []
for kmer, count in kmer_counts.items():
	if count == max_count:
		most_frequent_kmers.append(kmer)

print " ".join(most_frequent_kmers)
