x=int(input())
y=int(input())
if 1<=x<=10**12 and 1<=y<=10**12: 
	a=[]
	b=[]
	def ha(num):
		i=1
		while(i<=num):
			if(num % i==0):
				a.append(i)
			else:
				pass;
			i=i+1
	def haa(num):
		i=1
		while(i<=num):
			if(num % i==0):
				b.append(i)
			else:
				pass;
			i=i+1

	ha(x)
	haa(y)

	set1=set(a)
	set2=set(b)
	set3=set1 & set2
	print(len(set3))