'''
	Write a Program to Check if Given Number is Armstrong Number or Not
	
	Input: 153
	Output: Its a Armstrong Number
	
	Developed By: Parth Shah
	Python version: Python 3.7
'''

n = input("Enter Number to Check Armstrong or Not ")
sum = 0

for i in n:
	sum += (int(i)**3)

print("Given Number is ArmStrong") if int(sum)	== int(n) else print("Not a Armstrong")