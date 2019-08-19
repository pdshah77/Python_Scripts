'''
Python Program to add first and last element of list till single element
	Logic: input [1,3,4,7,9] 
		   output [1,3,4,7,9]
				  [10,3,4,7]
				  [17,3,4]
				  [21,3]
				  [24]
Designed By: Parth Shah
Python Version: Python 3.7
'''


def listProblem(list_ele):
	
	while len(list_ele) > 1:
		sum = list_ele[0] + list_ele[-1]
		list_ele = [sum] + list_ele[1:-1]
		print(' '.join(map(str,list_ele)))
	else:
		print("One or Less Element Present in List")
            

ele = list(map(int,input().split()))		
print(' '.join(map(str,ele))) 		# Since We want to Print First Raw as it is
a = listProblem(ele)
