'''
 Write a Program to print prime numbers less than 100 using for else statement
 
 Developed By: Parth Shah
 Python Version: Python 3.7 using For Else Loop
 Logic: Start from 2 and go upto Given Number and find modulos everytime, if reminder is zero given number is not prime Number
 '''

for i in range(2,100):
    for x in range(2, i):
        if i % x == 0:
            break
    else:
        # loop fell through without finding a factor
        print(i, 'is a prime number')