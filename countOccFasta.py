#!/usr/bin/env python
import sys
from Bio import SeqIO
seq = sys.argv[2]
count = 0
fastafile = open(sys.argv[1], "rU")
records = list(SeqIO.parse(fastafile, "fasta"))
fastafile.close()
for i in range(0,len(records)):
	if seq in records[i].seq:
		count += 1
print "Total Sequences:",len(records)
print "Sequences with",seq,":",count