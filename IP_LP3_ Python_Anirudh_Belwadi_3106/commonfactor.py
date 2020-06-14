x1=int(input())
x2=int(input())
if 1<=x1<=10**12 and 1<=x2<=10**12:
	l1=[]
	l2=[]
	for i in range(1,x1+1):
    		if x1%i==0:
        		l1.append(i)
	s1=set(l1)        
	for i in range(1,x2+1):
    		if x2%i==0:
        		l2.append(i)
	s2=set(l2)
	s3=s1.intersection(s2)
	print(len(s3))
