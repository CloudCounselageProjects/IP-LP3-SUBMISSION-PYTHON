n=int(input())
l=[input() for i in range(n)]
l2=[]
for i in range(len(l)):
    if l[i] not in l2:
        l2.append(l[i])
print(len(l2))
for i in range(len(l2)):
    print(l.count(l2[i]),end=' ')
