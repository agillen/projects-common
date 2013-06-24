#!/usr/bin/env python
# Removes DEXSeq results with a pvalue > than pval
# Usage: polyApval infile pval
import sys
for line in open(sys.argv[1]):
	fields = line.split('\t')
	try:
		pval = float(fields[4])
	except ValueError:
		continue
	if pval < float(sys.argv[2]):
		print line,
