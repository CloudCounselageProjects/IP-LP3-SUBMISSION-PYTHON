n=int(input('How many elements want:'))
l=[]
for i in range(n):
    p=int(input())
    l.append(p)
l.sort()
print(l)