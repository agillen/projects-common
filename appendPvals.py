#!/usr/bin/env python
# Appends pvals to miR fold 
# Usage: appendPvals.py X_to_Y.*.fold 
import sys
foldf = open(sys.argv[1]).readlines()
sixmerpval = open(sys.argv[1].replace(".mirs.fold",".run7mer.R.out")).readlines()
seqpval = open(sys.argv[1].replace(".mirs.fold",".runSeq.R.out")).readlines()
outf = [foldf[0]+foldf[1]+foldf[2].replace("\n","")+"\tpvalSeq\tpadjSeq\tpval7mer\tpadj7mer"]
for i in range(3,len(foldf)):
	seqpval[i-2] = seqpval[i-2].replace("\n","")
	sixmerpval[i-2] = sixmerpval[i-2].replace("\n","")
	outf.append(foldf[i].replace("\n","")+"\t"+seqpval[i-2].replace("[1] ","")+"\t"+sixmerpval[i-2].replace("[1] ",""))
outfile = open(sys.argv[1].replace(".mirs.fold",".mirs.final"), "w")
for item in outf:
	print>>outfile, item
