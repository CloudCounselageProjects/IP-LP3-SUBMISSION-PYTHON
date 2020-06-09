# problem number 1
a, b = map(int, input().split())    # To take multiple inputs
if 1 < a and b < pow(10,10): 
    sum1 = a + b                        # addition of numbers
    sub = a - b                         # Difference between two numbers
    mul = a * b                         # product of numbers
    print(sum1, sub, mul)               # display sum, difference, product of numbers in one line
