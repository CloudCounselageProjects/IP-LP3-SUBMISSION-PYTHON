l1=[]
n=int(input())
for i in range(n):
    st=input()
    l1.append(st)
    
set1=set(l1)
print(len(set1))
for i in set1:
    print(l1.count(i),end=' ')
