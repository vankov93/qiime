#
# GAGTTTGATCCTGGCTCAG#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn = 'non_chimeras.txt'
f = open(fn)
for line in f:
	nch=line
fn = 'chimeras.txt'
f = open(fn)
for line in f:
	ch=line
print("chimeras	"+ ch[:-1] + "	" + "non_chimeras	" + nch)
fn = 'split/split_library_log.txt'
f = open(fn)
print('	Total number of input sequences	Read too short after quality truncation	Median sequence length	Total number seqs written	chimeras')
line2=""
n=0
for line in f:
	if "Sequence read filepath:" in line and n==0:
		line2= line2+ line[24:32]+ "	"
	if "Sequence read filepath:" in line and n!=0:
		line2=line2+ line[24:32]+ "	"
		n=n+1
	if "Total number of input sequences:" in line:
		line2= line2+ line[33:-1]+ "	"
		n=n+1
	if "Read too short after quality truncation:" in line:
		line2= line2+ line[41:-1]+ "	"
		n=n+1
	if "Median sequence length:" in line:
		line2= line2+ line[23:-1]+ "	"
		n=n+1
	if "Total number seqs written" in line:
		line2= line2+ line[26:]
		n=n+1
print(line2)




#fn = '/home/qiime/testscript/joined/chimerac.txt'
#f = open(fn)
#for line in f:
	#line2=line2+line
