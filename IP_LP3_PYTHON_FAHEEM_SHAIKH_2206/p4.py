a=int(input())
b=int(input())
c=0
for i in range(1,min(a,b)):
    if(a%i==0 and b%i==0):
        c+=1
print(c)        
