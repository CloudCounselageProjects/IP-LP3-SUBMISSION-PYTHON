"""
Read two integers from STDIN and print three lines where:
● The first line contains the sum of the two numbers.
● The second line contains the difference between the two numbers (first - second).
● The third line contains the product of the two numbers. 
 
"""

a = int(input())                          #Read two integers
b = int(input())

if 1<=a<=10**10 and 1<=b<=10**10:         #constraints
 sum = a+b
 difference = a-b
 product = a*b
 print (sum)                              #The first line contains the sum of the two numbers.
 print (difference)                       #The second line contains the difference of the two numbers (first - second).
 print (product)            
