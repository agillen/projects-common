#!/usr/bin/env python
import random
import sys
from Bio import SeqIO
save = []
fastafile = open(sys.argv[1], "rU")
records = list(SeqIO.parse(fastafile, "fasta"))
fastafile.close()
for i in range(0,len(records)):
	if "hsa" in records[i].id:
		save.append(records[i])
out_file = open(sys.argv[1].replace(".fa",".hsa.fa"), "w")
SeqIO.write(save, out_file, "fasta")
out_file.close()
