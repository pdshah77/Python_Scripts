''' 
	A fixed point in an array is an element whose value is equal to its index. 
	Given a sorted array of distinct elements, return a fixed point, if one exists. 
	Otherwise, return False.
	
	Given [-6, 0, 2, 40], you should return 2
	
	Given [1, 5, 7, 8], you should return False
	
'''

def ValueIndex(array):
	# Since Assumption is to Find Unique Index Value only
	for i in range(len(array)):
		if i == array[i]:
			return i
			break
	else:
		return False
	
print(ValueIndex([1, 5, 7, 8]))

print(ValueIndex([-6, 0, 2, 40]))