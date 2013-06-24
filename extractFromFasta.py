#!/usr/bin/env python
import sys
import string
from Bio import SeqIO
seq = sys.argv[2]
count = 0
bed = []
fastafile = open(sys.argv[1], "rU")
records = list(SeqIO.parse(fastafile, "fasta"))
fastafile.close()
for i in range(0,len(records)):
	if seq in records[i].seq:
		fields = records[i].description.split(" ")		
		bedi = fields[1].translate(string.maketrans(':-','\t\t'))
		bed.append(bedi.replace("range=","")+"\t"+str(fields[0])+"\t0\t"+str(fields[4].replace("strand=","")))
for item in bed:
	print item

