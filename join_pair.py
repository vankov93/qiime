#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn = 'list.txt'
f = open(fn)
i=0
j=""
print("#!/bin/bash")
for line in f:
	if "R1"  in line:
		line3 = "join_paired_ends.py -f" + " " + line
		
	if "R2"  in line:
		line2 = " -r " + line.rstrip() + " -o joined;"
		print(line3.rstrip() + line2.rstrip())
		i=i+1
		j=line.rstrip()
		print("mv joined/fastqjoin.join.fastq" + " joined/" + j)



