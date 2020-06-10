#CODING QUESTIONS:​8 (This code was executed in Visual Studio Code)
#Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)...(until n-x =< 0).
# Test Data: sum_series(6) -> 12 sum_series(10) -> 30 
def sum_series(n):                      #The function name is described in the test data i.e. sum_series.
    if n < 1:
        return (0)
    else:
        return n + sum_series(n - 2)
print(sum_series(6))
print(sum_series(10))

#End of question 7