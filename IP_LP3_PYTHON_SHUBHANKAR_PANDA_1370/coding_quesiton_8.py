'''
Coding Question 8
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)...
(until n-x =< 0).
Test Data:
sum_series(6) -> 12
sum_series(10) -> 30
'''
def sum_series(n):
    sum1=0
    i=0
    while((n-i)>=0):
        sum1+=(n-i)
        i+=2
    return sum1    

print(sum_series(int(input())))    
