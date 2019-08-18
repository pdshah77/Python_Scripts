'''
 Write a Program to Print Even Numbers Less than 100
 
 Developed By: Parth Shah
 Python Version: Python 3.7 using List Comprehension
 '''

# 100 will not Include in this 
print("Even Number Starting from 0 to 99")
print([p for p in range(100) if p%2 == 0])

# If we have to include 100 also then range will be (0 to 101)
print("Even Number Starting from 0 to 101")
print([p for p in range(101) if p%2 == 0])