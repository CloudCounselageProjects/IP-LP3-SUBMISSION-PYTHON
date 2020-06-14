a=int(input())
b=int(input())
def gcd(a,b):
    if (a==0):
        return b
    return gcd(b%a, a)
if (a>0 and a<=(10**12) and b>=1 and b<=(10**12)):
    count=1
    for i in range(2,gcd(a,b)+1):
        if a%i==b%i==0:
            count+=1
    print(count)
    


"""
OUTPUT:
    
input:
10

15

output:
2

"""