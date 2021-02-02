def sum_series(n):
	sum=0
	while(n!=0):
		sum=sum+n
		n=n-2
	print(sum)
n=int(input())
sum_series(n)