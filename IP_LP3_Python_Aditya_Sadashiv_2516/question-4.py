n1=int(input())
n2=int(input())
l1=[]
l2=[]
for i in range(1,n1+1):
    if n1%i==0:
        l1.append(i)

set1=set(l1)        
   
for i in range(1,n2+1):
    if n2%i==0:
        l2.append(i)

set2=set(l2)
set3=set1.intersection(set2)
print(len(set3))
