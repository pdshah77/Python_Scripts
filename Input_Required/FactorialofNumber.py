''' 
	Write a Program to Find Factorial of a Given Integer Number
	Logic: Factorial Number is Multiplication of that Number till 1
	for 6 = 6 x 5 x 4 x 3 x 2 x 1 = 120

	Developed By: Parth Shah
	Python Version: Python 3.7
'''

n = int(input("Enter number to Find Factorial of a Number: "))

fact = 1

for i in range(1,n+1):
	fact = fact * i
	
print(fact)
