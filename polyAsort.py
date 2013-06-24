#!/usr/bin/env python
# Produces a list of sites present in both of two DEXSeq samples with the
# same directional fold-change.
# Usage: polyAsort DEXSeqFile1.txt DEXSeqFile2.txt outfilePrefix
import sys
sample1 = open(sys.argv[1]).readlines()
sample2 = open(sys.argv[2]).readlines()
passlist = []
faillist = []
genesyms = []
sin = []
mult = []
outfail = open(sys.argv[3] + "-fail.txt", "w")
outpass = open(sys.argv[3] + "-pass.txt", "w")
outsin = open(sys.argv[3] + "-pass.sin.txt", "w")
outmult = open(sys.argv[3] + "-pass.mult.txt", "w")
for line1 in sample1:
	fields1 = line1.split("\t")
	for line2 in sample2:
		if fields1[2] in line2:
			fields2 = line2.split("\t")
			if float(fields2[7]) * float(fields1[7]) > 0:
				fields2[7] = fields2[7].replace('\n','')
				fields2.append(fields1[7])
				passlist.append("\t".join(fields2))
			else:
				fields2[7] = fields2[7].replace('\n','')
				fields2.append(fields1[7])
				faillist.append("\t".join(fields2))
for item in faillist:
	print>>outfail, item,
for item in passlist:
	print>>outpass, item,
for line in passlist:
	fields = line.split("\t")
	genesyms.append(fields[1])
for line in passlist:
	fields = line.split("\t")
#	print fields[1]
#	print sample.count(fields[1])
	if genesyms.count(fields[1]) > 1:
		mult.append(line)
	else:
		sin.append(line)
for item in sin:
	print>>outsin, item,
for item in mult:
	print>>outmult, item,
