'''
	Write a Program to Find First Repeating Element in Given String
	Logic: For Given String abca
	Output should be a since a is repeating first
	
	Developed By: Parth Shah
	Python Version: Python 3.7
'''

inp_str = raw_input()
dicti = {}

for i in inp_str:
	if i in dicti:
		dicti[i] += 1
	else:
		dicti[i] = 1

res = 'NULL'					# Since No Element Repeats we will print NULL

for key,value in dicti.items():
	if value > 1:
		res = key
		break
	else:
		res = 'NULL'

print(res)
