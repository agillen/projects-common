#!/usr/bin/env python
# Generates R script to calculate significance of overrepresented miR sites
# (7mer-1A, 7mer-m8 and 8mers) based on output from seedsearch.py
# Usage: generateRscript.py testsample.mirs referencesample.mirs
import sys
sample1 = open(sys.argv[1]).readlines()
sample2 = open(sys.argv[2]).readlines()
cmds1 = ["pval <- numeric(0)"]
cmds2 = ["pval <- numeric(0)"]
Rstr1 = "pval <- c(pval,phyper("
Rstr2 = ",lower.tail=FALSE))"
outf = [sample1[0]+sample1[1]+sample1[2].replace("\n","")+"\tFrequency\tFold Over Ctl."]
for i in range(3,len(sample1)):
	fields1 = sample1[i].split("\t")
	fields2 = sample2[i].split("\t")
	cmds1.append(Rstr1+fields1[4]+"-1,"+fields2[4]+","+fields2[5].replace("\n","")+","+str(int(fields1[4])+int(fields1[5]))+Rstr2)
	cmds2.append(Rstr1+fields1[2]+"-1,"+fields2[2]+","+fields2[3]+","+str(int(fields1[2])+int(fields1[3]))+Rstr2)
	repr = float(fields1[2])/(int(fields1[2])+int(fields1[3]))
	if float(fields2[2])/(int(fields2[2])+int(fields2[3])) == 0:
		foldo = "N/A"
	else:
		foldo = repr/(float(fields2[2])/(int(fields2[2])+int(fields2[3])))
	outf.append(sample1[i].replace("\n","")+"\t"+str(repr)+"\t"+str(foldo))
cmds1.append("padj <- p.adjust(pval, method = \"BH\")\nframe <- data.frame(pval, padj)\nwrite.table(frame, \""+sys.argv[1].replace(".mirs",".run7mer.R.out")+"\", sep=\"\\t\", col.names=T, row.names=F)")
cmds2.append("padj <- p.adjust(pval, method = \"BH\")\nframe <- data.frame(pval, padj)\nwrite.table(frame, \""+sys.argv[1].replace(".mirs",".runSeq.R.out")+"\", sep=\"\\t\", col.names=T, row.names=F)")
outR1 = open(sys.argv[1].replace(".mirs",".run7mer.R"), "w")
for item in cmds1:
	print>>outR1, item
outR2 = open(sys.argv[1].replace(".mirs",".runSeq.R"), "w")
for item in cmds2:
	print>>outR2, item
outR3 = open(sys.argv[1].replace(".mirs",".mirs.fold"), "w")
for item in outf:
	print>>outR3, item
	
