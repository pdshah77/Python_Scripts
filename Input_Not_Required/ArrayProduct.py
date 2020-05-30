'''
	Write a Program to do Product of Array Except Self
	Input: [1, 2, 3, 4, 5]
	Output: [120, 60, 40, 30, 24]
	
	Logic: Initialize Result array with value 1
	1. Left Multiplication Array: Iterate Throught Given Array from Left Side and Update Result Array with Multiplication Result
	2. Right Multiplication Array: 
'''

def mulArray(a,n):
	# Final Prodct Array
	prod = [1]*n
	temp = 1
	#left Array Product
	for i in range(n):
		prod[i] = temp
		temp *= a[i]			# prod = [1,1,2,6,24]

	temp = 1
	# Right Array Product
	for i in range(n-1,-1,-1):
		prod[i]*= temp
		temp*= a[i]			
	
	print(prod)
	

a = [2,3,4,5,6]   #[360,240,180,144,120]
n = len(a)
mulArray(a,n)