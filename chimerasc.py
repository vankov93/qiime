#
# GAGTTTGATCCTGGCTCAG#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn = 'list2.txt'
f=open(fn)
n=1
m=sum(1 for l in open('list2.txt', 'r'))
print("#! /bin/bash")
for line in f:
	if n<(m):
		print('grep -c "' + "^" + str(n) + '_" ' +"chimeras/chimeras.txt" + " >> chimerac.txt")
		n=n+1
	

