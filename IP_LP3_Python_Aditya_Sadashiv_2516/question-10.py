n=int(input("Enter the length"))
l=[]
print("Enter the elements")
for i in range(n):
    x=int(input())
    l.append(x)

for i in range(n):
    for j in range(i,n):
        if(l[i]>l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)
