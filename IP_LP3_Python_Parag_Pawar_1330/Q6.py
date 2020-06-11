m = int(input())
n = int(input())

alist = []

for i in range(0,n):
    alist.append(list(input().split()))

maxrow = list()
minrow = list()
maxcol = list()
mincol = list()
templist = list()
for i in range(0,n):
    maxrow.append(max(alist[i]))
    minrow.append(min(alist[i]))

    for j in range(0,m):
        templist.append(alist[j][i])
    
    maxcol.append(max(templist))
    mincol.append(min(templist))
    templist=[]

#print(maxrow)
#print(minrow)
#print(maxcol)
#print(mincol)

finallist = maxrow+minrow+maxcol+mincol

print(len(set(finallist)))
