f = open("rep_set_tax_assignments.txt")
for line in f:
	if "c__;o__" not in line and "k__Archaea" not in line:
		print(line.split()[0])
		#print(line)
		
