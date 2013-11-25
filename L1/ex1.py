# Frequent Words Problem: Find the most frequent k-mers in a string.
# Input: A string Text and an integer k.
# Output: All most frequent k-mers in Text.

# python ex2.py dataset_2_4.txt

import sys

filename = sys.argv[1]

txt = open(filename)
seq = txt.readline().strip()
kmer_size = int(txt.readline())

kmer_counts = {}
for i in range(len(seq)-kmer_size+1):
	kmer = seq[i:i+kmer_size]
	if kmer not in kmer_counts:
	    kmer_counts[kmer] = 0
	kmer_counts[kmer] += 1

max_counted_kmers = []
max_kmer_counts = max(kmer_counts.values())
for kmer, count in kmer_counts.items():
    if count == max_kmer_counts:
    	max_counted_kmers.append(kmer)
print " ".join(max_counted_kmers)
