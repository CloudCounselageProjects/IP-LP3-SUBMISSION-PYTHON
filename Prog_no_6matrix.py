
m,n=map(int,input().split())
l1=[]
for i in range(n):
    l1.append(list(map(int,input().split())))
minormax=[]
#rowwise
for i in range(n):
    minormax.append(min(l1[i]))
    minormax.append(max(l1[i]))
l2=[]
for i in range(m):
    c=[]
    for j in range(n):
        c.append(l1[j][i])
    l2.append(c)
for i in range(m):
    minormax.append(min(l2[i]))
    minormax.append(max(l2[i]))

g= list(dict.fromkeys(minormax))
print(len(g))