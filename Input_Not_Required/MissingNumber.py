'''

	Write a Program to Find a missing number from Given N numbers of Array.
	Numbers can be in any order. No duplicates are present in the array.
	
	Example: a = [1,2,3,5]
	Output: 4
	
	Explanation: 1. Find Total Sum of All the Elements
	2. Subtract Sum of Array Elements from Total Sum
	'''
	
def MissingNumber(array):
	n = len(array)
	s = sum(array)
	totalSum = ((n+1)*(n+2))/2
	
	return totalSum - s

a = [1,2,4,6,3,7,8,5,9,11,12,15,13,14]
print(MissingNumber(a))