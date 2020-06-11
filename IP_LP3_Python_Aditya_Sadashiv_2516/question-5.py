l1=[]
set1=set()
for i in str1:
    if i not in set1:
        set1.add(i)
        l1.append(i)

str2=""
for i in range(len(l1)):
    str2=str2+l1[i]
print(str2)
