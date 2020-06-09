"""
CODING QUESTIONS:6
Given a matrix of size m*n, m denotes the row starting with index 0 and n denotes the
column starting with index 0.
The matrix will hold distinct integers as elements.
We need to find a distinct number of positional elements which are either the minimum
or maximum in their corresponding row or column.
"""
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