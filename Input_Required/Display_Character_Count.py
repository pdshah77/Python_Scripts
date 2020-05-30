''' 
	Write a Program to Display count of each characters in Given String.
	Logic: For Given String abcabccdecde output should be a:2, b:2, c:4, d:2, e:4
	
	Developed By: Parth Shah
	Python Version: Python 3.7
'''

inp_str = input()
dicti = {}

for ch in inp_str:
	if ch in dicti:
		dicti[ch] += 1
	else:
		dicti[ch] = 1

print(dicti)
		
