#!/usr/bin/env python
# Counts sequences in target file with matches to each microRNA seed site in input
# miRNA seed site list input format: "NAME\tSEED"
import sys
list = open(sys.argv[1]).readlines()
mirlist = open(sys.argv[2]).readlines()
seqs = int(sys.argv[3])
length = int(sys.argv[4])
allmiRs = []
mirtrack = []
mirsperseq = []
miRs = []
print "Total Sequences:",seqs
print "Total 7mers:",length
print "microRNA\t\tPresent(seq)\tAbsent(seq)\tPresent(7mer)\tAbsent(7mer)"
for line1 in list:
	fields = line1.split("\t")
	allmiRs.append(fields[3])
	mirtarget = fields[3]+fields[9]
	if mirtarget not in mirtrack:
		mirtrack.append(mirtarget)
		mirsperseq.append(fields[3])
for line2 in mirlist:
	mirname = line2.replace("\n","")
	count = allmiRs.count(mirname)
	countseq = mirsperseq.count(mirname)
	print line2.replace("\n","")+"\t\t"+str(countseq)+"\t"+str(seqs - countseq)+"\t"+str(count)+"\t"+str(length - count)
