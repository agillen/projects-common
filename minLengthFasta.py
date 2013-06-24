#!/usr/bin/env python
import random
import sys
from Bio import SeqIO
strip = []
fastafile = open(sys.argv[1], "rU")
records = list(SeqIO.parse(fastafile, "fasta"))
fastafile.close()
for i in range(0,len(records)):
	if len(records[i].seq) < 8:
		strip.append(records[i])
for i in range(0,len(strip)):
	records.remove(strip[i])
out_file = open(sys.argv[1].replace(".fa",".min8.fa"), "w")
SeqIO.write(records, out_file, "fasta")
out_file.close()
