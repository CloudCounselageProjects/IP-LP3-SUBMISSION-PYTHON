
dict1 = {}
a=input()
a1=[]
a2=""
for i in range(len(a)):
    a1.append(a[i])
    
for i in range(len(a)):
    
    key = a[i]
    if not key in dict1.keys():
        dict1.update({key : 1})
    else:
        dict1[key] += 1


for i in dict1.keys():
    a2+=str(i)


print(a2)    
    
