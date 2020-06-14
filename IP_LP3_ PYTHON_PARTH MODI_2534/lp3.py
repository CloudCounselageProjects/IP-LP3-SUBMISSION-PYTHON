x=int(input())
if (1<=x<=10**5):
	helloString =[]
	for i in range(x):
		y=(input())
		helloString .append(y)



	count = {}
	c=0;
	for word in helloString :
		if word in count :
			count[word] += 1
		
		
		else:
			count[word] = 1
			c=c+1

	print(c)

	for i in count:
		print(count[i],end="  ")
	
