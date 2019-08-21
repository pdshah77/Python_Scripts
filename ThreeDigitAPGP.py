'''
	Write a Program to Find Three Digit Terms when seen from left to right forms a 
	Term of A.P or G.P.
	
	Developed By: Parth Shah
	Python Version: Python 3.7
	
	Logic: For AP: Find Difference Between Second and First Digit which should be equal to Third and Second Digit
		   For GP: If third Digit is Equal to Square of Second Digit Divide by First Digit 
'''

ap_result = []

for ele in range(100,1000):
	temp = str(ele)
	
	# Condition for AP is Difference Should be Constant
	if int(temp[1])-int(temp[0]) == int(temp[2])-int(temp[1]):
		ap_result.append(temp)								
	
	# Condition for GP is Multiplication should be Constant
	if float(temp[2]) == ((float(temp[1])*float(temp[1]))/float(temp[0])):
		if temp not in ap_result:
			ap_result.append(temp)

print("Length of AP Results", len(ap_result))

print("Elements of AP", ' '.join(ap_result))


