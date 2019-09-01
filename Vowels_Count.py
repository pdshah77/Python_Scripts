''' 
	Write a Program to Count number of vowels using set
	From a Given String count the number of Vowels 
	
	Developed By: PARTH SHAH
	Python Version: Python 3.7
'''

def vowels_count(inp_str):
	vowels = set('aAeEiIoOuU')
	count = 0
	for ele in inp_str:
		if ele in vowels:
			count += 1
	return count
	
	
inp_str = input()
print(vowels_count(inp_str))