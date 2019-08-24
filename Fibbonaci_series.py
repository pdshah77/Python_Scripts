''' 
	Write a Program to Find Fibbonacci Series upto n
	
	Input: n = 5
	Output: 1,1,2,3,5

	Developed By: Parth Shah
	Python Version: Python 3.7
	
'''
import sys
try:
	n = int(input("Enter Number to Find Fibonnaci Series Upto "))
except ValueError:
	print("Given Input is Not a Valid")	
	sys.exit()

def Fibbonacci(n):
	
	a = 0
	b = 1

	res = [a,b]

	for _ in range(2,n+1):
		c = a + b
		a = b
		b = c
		res.append(c)

	if n < 2:
		print(res[0])
	else:
		for ele in res:
			print(ele , end=" ")
	
Fibbonacci(n)