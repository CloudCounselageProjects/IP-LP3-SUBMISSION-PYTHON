l=[int(input()) for i in range(int(input()))]
for i in range(len(l)-1):
    min=i
    for j in range(i+1,len(l)):
        if(l[min]>l[j]):
            min=j
    l[i],l[min]=l[min],l[i]
print(l)