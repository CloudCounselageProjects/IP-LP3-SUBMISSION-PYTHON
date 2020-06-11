n=int(input())
output=0
if (n>=0):
    for i in range(n):
        output=output+n
        n=n-2
        if (n==0):
            break
print(output)