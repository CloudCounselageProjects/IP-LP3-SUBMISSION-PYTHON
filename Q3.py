n=int(input())
list=[]
for i in range(n):
    p=input()
    list.append(p)
print(len(set(list)))
for item in list:
    print(list.count(item),end=" ")