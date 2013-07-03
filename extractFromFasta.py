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
#		fields = records[i].description.split(" ")		
		bedi = records[i].id.translate(string.maketrans(':-','\t\t'))
		bedi = bedi.replace(")","")
		bed.append(bedi.replace("(","\t.\t0\t"))
for item in bed:
	print item

