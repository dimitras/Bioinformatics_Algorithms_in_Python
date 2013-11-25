# Clump Finding Problem: Find patterns forming clumps in a string.
# Input: A string Genome, and integers k, L, and t.
# Output: All distinct k-mers forming (L, t)-clumps in Genome.

# python ex4.py ex4.txt

import sys

filename = sys.argv[1]

txt = open(filename)
seq = txt.readline().strip()
(k,L,t) = txt.readline().strip().split(' ')

max_counted_kmers = set()
for i in range(len(seq)-int(L)+1):
	seqL = seq[i:i+int(L)]

	kmer_counts = {}
	for i in range(len(seqL)-int(k)+1):
		kmer = seqL[i:i+int(k)]
		if kmer not in kmer_counts:
		    kmer_counts[kmer] = 0
		kmer_counts[kmer] += 1
	
	for kmer, count in kmer_counts.items():
	    if count >= int(t):
	    	max_counted_kmers.add(kmer)

print " ".join(max_counted_kmers)
