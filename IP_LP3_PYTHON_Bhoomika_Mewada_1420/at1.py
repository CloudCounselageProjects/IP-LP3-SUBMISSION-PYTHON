"""CODING QUESTIONS: 1
Read two integers from STDIN and print three lines where:
● The first line contains the sum of the two numbers.
● The second line contains the difference between the two numbers (first -
second).
● The third line contains the product of the two numbers.
"""
#   n is an integer list of two nos
n=list(map(int,input.split()))
#sum of two nos
print(n[0]+n[1])
#difference of two nos(first-second)
print(n[0]-n[1])
#product of two nos
print(n[0]*n[1])