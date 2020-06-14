l=[]
n=int(input())
if 1<=n<=10**5:
	for j in range(n):
		x=input()
		l.append(x) 
	s=set(l)
	print(len(s))
	for i in s:
		if len(i)>=10**6:
			exit()
		i=lower(i)
	for i in s:
    		print(l.count(i),end=' ')
	print()
