'''
	Given an array of integers, arr, where all numbers occur twice except one number which occurs once,
	find the number. Your solution should ideally be O(n) time and use constant extra space.
'''

# Below Solution works in O(n) time, but requires extra space
class Solution(object):
	def findSingle(self, nums):
    # Fill this in.
		dict = {}
		for ele in nums:
			if ele in dict:
				dict[ele]+=1
			else:
				dict[ele]=1
		
		for key,value in dict.items():
			if dict[key] == 1:
				return key

nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3


# Use XOR Logic to Calculate in O(n) time and no extra space
def findSingle( ar, n):  
	res = ar[0] 
    # Do XOR of all elements and return 
	for i in range(1,n): 
		res = res ^ ar[i]
	return res

print(findSingle(nums,len(nums)))