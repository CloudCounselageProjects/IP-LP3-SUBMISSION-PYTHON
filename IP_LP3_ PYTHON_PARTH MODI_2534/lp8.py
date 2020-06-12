n=int(input())
x=0
def sum(n):
	
	if(n==0):
		return 0
	else:
		global x
		x= x + n
		sum(n-2)
		return x;
y=(sum(n))
print(y)

	