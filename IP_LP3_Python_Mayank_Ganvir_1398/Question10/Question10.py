a=[14,46,43,27,57,41,45,21,70]
i=0
while i<len(a):
    sm=min(a[i:])
    id=a.index(sm)
    a[i],a[id]=a[id],a[i]
    i=i+1
print(a)