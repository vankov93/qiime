#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn = 'list.txt'
f = open(fn)
for line in f:
	print("convert_fastaqual_fastq.py -f " + line + " -o fasta -c fastq_to_fastaqual") 


