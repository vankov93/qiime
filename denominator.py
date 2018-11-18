f = open('/home/qiime/16sAM/joined/rarefied/taxasum/otus_sort_L6.txt')
for line in f:
	#print(line)
	list = line.split()
	for i in range(len(list)):
		#print(list)
		if ";Other" in list[i]:
			list[i] = list[i][(list[i].rfind('__')-1):list[i].index(";Other")]
		if ';g__' in list[i]  and list[i][-3:] != 'g__':
			
			list[i] = list[i][list[i].index('g__'):]
		if ';g_' in list[i]:
			if ";f__;" not in list[i]:
				list[i] = list[i][list[i].index('f__'):list[i].index(';g__')]
			else:
				if ';o__;' in list[i] and 'c__;' not in list[i]:
					list[i] = list[i][list[i].index('c__'):list[i].index(';o__;')]
				elif ';o__' in list[i] and ';o__;' not in list[i]:
					list[i] = list[i][list[i].index('o__'):list[i].index(';f__;')]
				elif 'c__;' in list[i]:
					list[i] = list[i][list[i].index('p__'):list[i].index(';c__;')]
	st=''
	for l in list:
		st=st+' '+l
	print(st)





			
			

