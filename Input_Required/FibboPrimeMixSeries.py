''' 
	From a Given mixture of 2 series - all odd terms form a Fibonnaci series and 
	all even terms form the prime numbers in ascending order.
	
	Write a program to find Nth term in this series
	Given Series: 1,2,1,3,2,5,3,7,5,11,8,13,13,17,..
	Developed By: Parth Shah
	Python Version: Python 3.7
	
	
'''

def Fibbonaci(n):
	if n==0:
		return 1
	elif n==1:
		return 1
	else:
		return Fibbonaci(n-1)+Fibbonaci(n-2)
		
def Prime_Num(n):
	prime_no = [2]
	num = 3
	while len(prime_no) < n:
		for ele in prime_no:
			if num % ele == 0:
				break
		else:
			prime_no.append(num)
		num += 2	
	return prime_no[-1]
	
inp_no = int(input("Enter the term to find "))

if inp_no % 2 == 0:
	print("Prime Number Series Finder")
	inp_no //= 2      # For All EVEN NUMBERS PRIME NUMBER
	print(Prime_Num(inp_no))
	
else:
	print("Fibonnaci Finder")
	inp_no = (inp_no//2)+1  # For All ODD NUMBERS 
	print(Fibbonaci(inp_no-1))
