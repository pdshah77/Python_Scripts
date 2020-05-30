'''
	Write a Program to arrange given list of numbers 
	to form the largest possible integer
	
	Input: i) [10,7,76,415]  ii) [54, 546, 548, 60]  iii)[1, 34, 3, 98, 9, 76, 45, 4]
	Output: 7764150				 6054854654				  998764543431
	
	Developed By: Parth Shah
	Python Version: Python 3.7
'''

from itertools import permutations

l = [1, 34, 3, 98, 9, 76, 45, 4]
result = []

# Permutations will list out all possible results
for i in permutations(l,len(l)):
	result.append("".join(map(str,i)))		#Storing in List

print(max(result))