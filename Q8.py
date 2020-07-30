n=int(input())
op=0
for x in range(0,n,2):
    if(n-x>=0):
        op+=(n-x)
print("sum_series("+str(n)+")->" +str(op))