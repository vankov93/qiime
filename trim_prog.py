#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn = 'list.txt'
f = open(fn)
i = 0
n = 0
k= ""
l= ""
for line in f:
	k = l
	l = line
	n=n+1
	i=i+1
	if i > 0 and (n%2) == 0:
		print("java -jar /home/qiime/Trimmomatic-0.36/trimmomatic-0.36.jar PE -phred33" + " " + k + " " + l + " " + "out/" + str(n) + "output_forward_paired" + k + " " +  "out/output_forward_unpaired"  + " " "out/" + str(n+1) + "output_reverse_paired" + l + " " + "out/output_reverse_unpaired" + " " + "ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:100")


