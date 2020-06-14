a=int(input())
b=int(input())
mini=min(a,b)
i=1
n=0
while(mini>1):
    if a%i==b%i==0:
        n=n+1
        mini//n
    i+=1
print(n)
