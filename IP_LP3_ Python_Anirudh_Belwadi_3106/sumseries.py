def sum_series(n):
    sum=0
    for x in range(0,n,2):
        sum=sum+(n-x)
        if(n-x<=0):
            break;
    print(sum)    
n=int(input())
sum_series(n)
