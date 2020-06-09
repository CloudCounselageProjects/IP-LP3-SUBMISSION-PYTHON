"""
CODING QUESTIONS:8
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)...
(until n-x =< 0).
"""
n=int(input())
sum1=0
for i in range(n,0,-2):
    sum1+=i
print(sum1)