#
# GAGTTTGATCCTGGCTCAG#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn = 'chimerac.txt'
f = open(fn)
n=1
for line in f:
	print(str(n) + " " + line[:-1])
	n=n+1

