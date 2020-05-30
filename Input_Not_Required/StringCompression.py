'''
	Write a Program to compress given an array of characters with repeats,
	
	Comparison should be less than or equal to the original array.
	
	Input: ['a','a','b','c','c','c']
	Output: ['a','2','b','c','3']
'''

class Solution(object):
	def compress(self,chars):
		dict = {}
		resList = list()
		# Added Elements in New Dictionary
		for ele in chars:
			if ele in dict:
				dict[ele] += 1
			else:
				dict[ele] = 1
				
		#Fetching Data from Sorted Dictionary
		for key,value in sorted(dict.items()):
			if value > 1:
				resList.append(key)
				resList.append(str(value))
			else:
				resList.append(key)
		return resList
		
print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))