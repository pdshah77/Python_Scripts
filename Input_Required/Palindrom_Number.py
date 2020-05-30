''' 
	Write a Program to find if given String is plindrome or not
	
	Developed By: Parth Shah
	Python Version: Python 3.7 using three different Techniques
	Logic: Given String is Known as Palindrom if you read from backside it reads same as Input
	Manual Input Required
'''

#Solution 1: Using String Reverse Function
'''
a = input()

if a == a[::-1]:
	print('Gievn String is Palindrom')
else:
	print('Given String is not palindrom')
	
'''

# Solution 2: Using Foreach Loop
'''
a = input()
result_str = ''
for ch in a:
	result_str = ch + result_str
	
if a == result_str:
	print("Palindrom")
else:
	print("Not Palindrom")
'''

#Solution 3: For Number Specifically
import sys

def get_int():
    userdata = input("Enter an int, or 'q' to quit: ")
    if userdata == 'q':
        sys.exit()
    try:
        user_num = int(userdata)
        return user_num
    except ValueError:
        print("I need an integer to continue.")
        return(get_int())	  

input_no = get_int()
temp = input_no
rev = 0
while(input_no>0):
	
	div = input_no%10
	rev = rev*10 + div
	input_no = input_no//10
	
if temp == rev:
	print('Palindrom')
else:
	print('Not Palindrom')