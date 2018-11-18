#
# GAGTTTGATCCTGGCTCAG#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn = 'list2.txt'
f = open(fn)
n=0
i=0
for line in f:
	n=n+1
n=n+1
print(n)
fn = '/home/qiime/ETALON/Fasting_Map.txt'
f = open(fn)
for line in f:
	if i<n:
		print(line[:-1])
		i=i+1
