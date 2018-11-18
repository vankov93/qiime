listo = []
f = open("rep_set_tax_assignments.txt")
for line in f:
	if "k__unidentified" not in line and "k__Protista" not in line and "k__Chromista" not in line and "k__Plantae" not in line:
		listo.append(line.split()[0])
		#print(line)
	else:
		print(line)
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

print(len(l2))
l2.sort()
j=len(l2)/100
print(len(set(l2)))
f.close()
f = open("norm.fna")
f2 = open('fnorm.fna', 'w')
s = 0
k = 0
for line in f:

	if ">" in line:

		h = 0
		l = 0
		r=len(l2)-1
    #print(l2,r)
		p = ((l+r)//2)

		while l <= r:
			p = ((l+r)//2)
        #print('i', 'l', 'r', 'p', 'a[p]')
        #print(k[i], l, r, p, a[p])
        #print(i, a[p])
			if l2[p] == line.split()[0][1:]:
				f2.write(line.strip() + '\n')
				#l2.remove(line.split()[0][1:])
				k = k+1
				#print(str(round(k/j, 1)) + "% complited")
				#print(len(l2))
				s = 1
				h = 1
				break
			elif l2[p] > line.split()[0][1:]:
				r = p-1
            #print(r)
			elif l2[p] < line.split()[0][1:]:
				l = p+1
            #print(i)


		else:
			s = 0
	if ">" not in line and s == 1:
		f2.write(line.strip() + '\n')
f.close()
f2.close()
exit()			






