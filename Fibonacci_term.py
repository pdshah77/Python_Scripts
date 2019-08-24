'''
	Write a Program to Print Fibbonaci Term Present at Given User Input
	
	Input: n = 5
	Output : 3
	
	Developed By: Parth Shah
	Python Version: Python 3.7
'''

import sys
try:
	n = int(input("Enter Number to Find value in Fibbo Series "))
except ValueError:
	print("Invalid Input! Try Again!")
	sys.exit()

def Fibbo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return Fibbo(n-1)+Fibbo(n-2)

print(Fibbo(n))

# Test Cases

assert Fibbo(5) == 5
assert Fibbo(4) == 3
assert Fibbo(9) == 34