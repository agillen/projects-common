#!/usr/bin/env python
# Converts microRNA seed site lists in "NAME\tSEED" format to clover format
import sys
import string
seedseqs = open(sys.argv[1])
def rc(dna):
	return dna.translate(string.maketrans('ACGTU','TGCAA'))[::-1]
for line in seedseqs:
        fields = line.split("\t")
	seed = rc(fields[1])
        print ">" + fields[0]
        for i in range(7):
		if seed[i] is 'A':
			print "1 0 0 0"
                if seed[i] is 'C':
                        print "0 1 0 0"
                if seed[i] is 'G':
                        print "0 0 1 0"
                if seed[i] is 'T':
                        print "0 0 0 1"
