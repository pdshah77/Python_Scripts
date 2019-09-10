'''
	Write a Program to reverse the order of characters in each word 
	within a sentence while still preserving whitespace and initial word order.
	
	Input: "The cat in the hat"
	Output: "ehT tac ni eht tah"
	
'''

class Solution:
	def reverseWords(self, str):
		temp_list1 = str.split()
		temp_list2 = []
		for ele in temp_list1:
			temp_list2.append(ele[::-1])
		return (' '.join(temp_list2))
	

assert Solution().reverseWords("The cat in the hat") == "ehT tac ni eht tah"
# ehT tac ni eht tah

assert Solution().reverseWords("Parth Shah") == "htraP hahS"
