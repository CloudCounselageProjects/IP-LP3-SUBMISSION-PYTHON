n=int(input())
a=[]
for k in range(0,n):
	y=int(input())
	a.append(y)
for i in range(n):
	min=i
	for j in range(i+1,n):
		if a[min]>a[j]:
			min=j
	a[i],a[min]=a[min],a[i]
print(a)		
		
	
