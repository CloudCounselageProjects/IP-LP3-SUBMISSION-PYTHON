n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
c=0
for i in range(1, min(n1,n2)+1):
    if n1%i == n2%i == 0:
        c+=1
print(c)
