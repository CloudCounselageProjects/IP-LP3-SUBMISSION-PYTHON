"""
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... 
(until n-x =< 0).  
Test 
"""
def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# change this value for a different result
num = 16

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))
