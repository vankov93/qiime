listo = []
f = open("rep_set_tax_assignments.txt")
for line in f:
	if "c__;o__" not in line and "k__Archaea" not in line:
		listo.append(line.split()[0])
		#print(line)
f.close()

f = open("final_otu_map.txt")
l2 = []
for line in f:
	l = line.split()
	if l[0] in listo:
		#print(len(l))
		for i in l:
			if "_" in i:
				l2.append(i)
f.close()
f = open("norm.fna")
f2 = open('fnorm.fna', 'w')
for line in f:
	s = 0
	if ">" in line:
		if line.split()[0][1:] in l2:
			f2.write(line.strip() + '\n')
			s = 1
	if ">" not in line and s = 1:
		f2.write(line.strip() + '\n')
f.close()
f2.close()			
