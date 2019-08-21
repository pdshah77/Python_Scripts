'''
	Write a Program to Find Greatest Common Denominator 
	Between Given Numbers
	
	Input: [42,56,14]
	Output: 14
	
'''

list = [42,56,14]

def find_gcd(x,y):
	while(y):
		x,y = y,x%y
	return x

gcd = find_gcd(list[0],list[1])

for i in range(2,len(list)):
	gcd = find_gcd(gcd,list[i])

print(gcd)