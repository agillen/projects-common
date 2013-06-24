#!/usr/bin/env python
import random
import sys
from Bio import SeqIO
dupes = []
mirs = []
with open(sys.argv[1], "rU") as fastafile:
	records = list(SeqIO.parse(fastafile, "fasta"))
for i in range(0,len(records)):
	if str(records[i].seq[1:8]) in dupes:
		for k in range(0,len(mirs)):
			if str(records[i].seq[1:8]) in str(mirs[k].seq[1:8]):
				mirs[k].id = mirs[k].id+","+records[i].id
	else:
		dupes.append(str(records[i].seq[1:8]))
		mirs.append(records[i])
out_file = open(sys.argv[1].replace(".fa",".uniq.fa"), "w")
SeqIO.write(mirs, out_file, "fasta")
out_file.close()
