# question 10

n = int(input('enter the size of the list\n'))
l1 = []
print('enter the elements of the list')
for item in range(n):
    n = int(input())
    l1.append(n)

for i in range(len(l1)-1):
    min_pos=i
    for j in range(i,len(l1)):
        if l1[min_pos]>l1[j]:
            min_pos=j
    temp = l1[i]
    l1[i]=l1[min_pos]
    l1[min_pos]=temp

print(l1)
