#!/usr/bin/env python
# Removes DEXSeq results with a pvalue > than pval
# Usage: polyApval infile pval
import sys
for line in open(sys.argv[1]):
	fields = line.split('\t')
	peak = int(fields[1])+30
	start = int(fields[7])
	end = int(fields[8])
	if peak < start:
		position = 0
	elif peak > end:
		position = 100
	else:
		position = (peak-start)*100/(end-start)
	if fields[11] is "-":
		position = 100 - position
	print position
