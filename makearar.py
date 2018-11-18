#
# GAGTTTGATCCTGGCTCAG#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn = 'nreads.txt'
n=0
i=0
a=""
b=0
f = open(fn)
for line in f:
	i=i+1
	if i>3:
		a=(line[:-1])
		if len(a)>2:
			b=int(a)
			if b>n:
				n=b
print("alpha_rarefaction.py -i otus_sort.biom -m Fasting_Map.txt -o arare -p /home/qiime/ETALON/alpha_params.txt -t open/rep_set.tre -n 10 -a -f -e" + " " + str(((round(n/10000)-1)*10000)))

