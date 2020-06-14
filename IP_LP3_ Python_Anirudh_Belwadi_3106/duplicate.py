str1=input()
l1=[]
s1=set()
for j in str1:
    if j not in s1:
        s1.add(j)
        l1.append(j)

str2=""
for j in range(len(l1)):
    str2=str2+l1[j]
print(str2)
