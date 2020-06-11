def sum_series(n):
    sum1=0
    for x in range(0,n,2):
        sum1=sum1+(n-x)
        if(n-x<=0):
            break;
    print(sum1)    

n=int(input())
sum_series(n)
