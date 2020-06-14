def sum_series(n):
    x=0
    sum=0
    while(n-x>0):
        sum=sum+(n-x)
        x=x+2
    return sum
n=int(input())
print(sum_series(n))