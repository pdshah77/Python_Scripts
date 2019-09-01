'''
	Write a Program to Find Trailing Zeros in a Factorial of a Number
	Example: For 5! = 120 trailing zero is 1
			 For 10! = 3628800 trailing zero are 2
			 For 4! = 24 Not Poosibble
			 
	Developed By: PARTH SHAH
	Python Version:Python 3.7
'''

def TrailingZeros(number):
	i = 5 
	count = 0
	while (number//i >= 1):
		count += number//i
		i *= 5
	return count
	
n = int(input("Enter number for which you want to find trailing Zeros "))
count = TrailingZeros(n)
print(count) if count else print("No Trailing Zeros")