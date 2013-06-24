#!/usr/bin/env python
# Appends site location class (5' UTR, ORF, 3' UTR) to polyA DEXSeq results
# Usage: polyAclass DEXSeqFile.txt SiteClassKey.txt
import sys
testres = open(sys.argv[1]).readlines()
sitekey = open(sys.argv[2]).readlines()
outlist = []
outfile = open(sys.argv[1].replace('.txt','.class.txt'), "w")
for line1 in testres:
	fields1 = line1.split("\t")
	fields1[len(fields1)-1] = fields1[len(fields1)-1].replace('\n','')
	fields1.append('')
	for line2 in sitekey:
		if fields1[2].replace('Ep.c','p.c') in line2:
			fields2 = line2.split("\t")
			fields1[len(fields1)-1] = str(fields1[len(fields1)-1].replace('\n',''))+(fields2[1])
	outlist.append("\t".join(fields1))
for item in outlist:
	print>>outfile, item,
