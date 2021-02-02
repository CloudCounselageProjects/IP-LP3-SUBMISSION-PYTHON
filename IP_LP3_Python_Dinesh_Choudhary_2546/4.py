n1=int(input())
n2=int(input())
'''
l,u=[],[]
for i in range(1,n1+1):
	if n1%i==0:
		l.append(i)
for i in range(1,n2+1):
	if n2%i==0:
		u.append(i)
l=set(l)
u=set(u)
z=l & u
count=0
for d in z:
	count=count+1
print(count)
'''
if n1>n2:
	n1,n2=n2,n1
if n2>n1:
	count=0
	for i in range(1,n2+1):
		if n1%i==0 and n2%i==0:
			count=count+1
print(count)