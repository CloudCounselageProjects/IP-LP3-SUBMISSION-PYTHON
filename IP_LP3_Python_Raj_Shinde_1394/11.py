#problem number 8
n = int(input())
x,sum = 0,0
while(n-x >= 0):
    sum = sum + n-x
    x = x + 2
print(sum)