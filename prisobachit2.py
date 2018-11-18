#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn = 'big.qual'
f = open(fn)
for line in f:
	if ">"  in line:
		print(line)
	if ">"  not in line and "3" in line:
		line = "35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 " + line
		print(line)		



# GAGTTTGATCCTGGCTCAG
