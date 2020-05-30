'''
	Given two arrays, write a function to compute their intersection - the intersection means the numbers that are in both arrays.
	
	Input: nums1 = [1,2,2,1], nums2 = [2,2]
	Output: [2]
	
	Note:
		Each element in the result must be unique.
		The result can be in any order.
		
'''

class Solution:
	def intersection(self, nums1, nums2):
		lena = len(nums1)
		lenb = len(nums2)
		result = []
		if lena > lenb:
			for ele in nums2:
				if ele in nums1:
					result.append(ele)
		else:
			for ele in nums1:
				if ele in nums2:
					result.append(ele)
		return list(set(result))			# Since Each Element in the result must be unique.
	

print(Solution().intersection([1,2,2,1], [2,2]))
# [9, 4]