a=int(input())
b=int(input())

c=max(a,b)
count=0
for i in range(1,c):
    if(a%i==0 and b%i==0):
        count=count+1

print(count)
    
