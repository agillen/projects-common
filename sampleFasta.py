#!/usr/bin/env python
import random
import sys
from Bio import SeqIO
seqs = int(sys.argv[2])
lengths = int(sys.argv[3])
filenum = int(sys.argv[4])
strip = []
fastafile = open(sys.argv[1], "rU")
records = list(SeqIO.parse(fastafile, "fasta"))
fastafile.close()
for i in range(0,len(records)):
	if len(records[i].seq) < lengths:
		strip.append(records[i])
for i in range(0,len(strip)):
	records.remove(strip[i])
for ofnum in range(1,filenum+1):
	recsample = random.sample(records, seqs)
	for i in range(0,len(recsample)):
		num1 = random.randint(0,len(recsample[i].seq)-lengths)
		recsample[i].seq = recsample[i].seq[num1:num1+lengths]
	out_file = open(sys.argv[1].replace(".fa","-rand"+str(ofnum)+".fa"), "w")
	SeqIO.write(recsample, out_file, "fasta")
	out_file.close()
