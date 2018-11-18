f = open("/home/qiime/150118beatles/bac/joined/taxasum/otus_sort_L6.txt")
for line in f:
	keep = 0
	if "0" not in line:
		print(line.strip())
	else:
		line2 = line
		line = line.split()
		for i in line:
			
			if "0" in i and "_" not in i:
				if float(i) > 0.01:
					
					keep = 1
					
		if keep == 1:
			print(line2.strip())
				
