#!/usr/bin/env python
# Counts sequences in target file with matches to each microRNA seed site in input
# miRNA seed site list input format: "NAME\tSEED"
import sys
import string
from Bio import SeqIO
fastafile1 = open(sys.argv[1], "rU")
targets = list(SeqIO.parse(fastafile1, "fasta"))
fastafile1.close()
fastafile2 = open(sys.argv[2], "rU")
mirseeds = list(SeqIO.parse(fastafile2, "fasta"))
fastafile2.close()
def rc(dna):
	return dna.translate(string.maketrans('ACGTU','TGCAA'))[::-1]
totallen = 0
for ln in range(0,len(targets)):
	totallen += len(targets[ln].seq) - 6
print "Total Sequences:",len(targets)
print "Total 7mers:",totallen
print "microRNA\tSeed+1\tPresent(seq)\tAbsent(seq)\tPresent(7mer)\tAbsent(7mer)"
for k in range(0,len(mirseeds)):
	count = 0
	count2 = 0
	for i in range(0,len(targets)):
		if rc(str(mirseeds[k].seq[1:8])) in targets[i].seq:
			count += 1
		elif rc(str(mirseeds[k].seq[1:7]))+"A" in targets[i].seq:
			count += 1
		count2 += targets[i].seq.count(rc(str(mirseeds[k].seq[1:8]))) + targets[i].seq.count(rc(str(mirseeds[k].seq[1:7]))+"A") - targets[i].seq.count(rc(str(mirseeds[k].seq[1:8]))+"A")
	print mirseeds[k].id+"\t"+mirseeds[k].seq[1:8]+"\t"+str(count)+"\t"+str(len(targets)-count)+"\t"+str(count2)+"\t"+str(totallen-count2)
