#
# GAGTTTGATCCTGGCTCAG#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn = 'list.txt'
f = open(fn)
l=0
l2=""
line3=""
k=1
n=0
print("#!/bin/bash")
for line in f:
	n=n+1
	l=len(line)
	l2=line[(l-9):-7]
	l=int(l2)
	while k <l:
		line3=line3+(str(k))+","
		k=k+1
	if k==l:
		
		line3=line3+(str(k))
	print("split_libraries_fastq.py -i " + line[:-1] + " -o split --sample_ids " + str(n) + " -q 19 --barcode_type 'not-barcoded'")

