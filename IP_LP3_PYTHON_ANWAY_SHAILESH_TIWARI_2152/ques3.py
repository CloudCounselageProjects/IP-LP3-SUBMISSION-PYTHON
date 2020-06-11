# question 3

n = int(input())
l = []
x = []
for i in range(n):
    l.append(input())

for i in range(n):
    if(l[i] not in l[0:i]):
        print(l[i],l.count(l[i]),end=' ')
