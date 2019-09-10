''' 
	Write a Program to find Running Median
	You are given a stream of numbers. Compute the median for each new element 
	Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]
	
	Logic:
	Median: Sort Given Numbers in Ascending Order 
	If Length of Array is Even then Median is Avg of Mid two terms
	If length of Array is Odd then Median is Middle term of Length Array
	
	Input: [2,1,4,7,2,0,5]
	[2] --> 2
	[2,1] --> [1,2] --> (2+1)/2 --> 1.5
	[2,1,4] --> [1,2,4] --> 2
	[2,1,4,7] --> [1,2,4,7] --> (2+4)/2 --> 3
	[2,1,4,7,2] --> [1,2,2,4,7] --> 2
	[2,1,4,7,2,0] --> [0,1,2,2,4,7] --> (2+2)/2 --> 2
	[2,1,4,7,2,0,5] --> [0,1,2,2,4,5,7] --> 2
	Final Answer: 2,1.5,2,3,2,2,2
	'''
def running_median(stream):
	temp = []
	count=0
	for ele in stream:
		temp.append(ele)
		temp.sort()
		if (len(temp)% 2 == 0):
			print(even_median(temp,count),end=' ')
			count += 1
		else:
			print(odd_median(temp),end=' ') # Odd Series Median
			
def odd_median(list):
	return list[0] if (len(list)-1) == 0 else list[(len(list)-1)//2]

def even_median(list,count):
	return ((list[count]+list[count+1])/2)

#running_median([2, 1, 4, 7, 2, 0, 5])
# 2 1.5 2 3.0 2 2.0 2

running_median([5,15,1,3])
# 2 2.0 2 2.5