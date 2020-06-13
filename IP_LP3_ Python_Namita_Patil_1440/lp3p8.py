#CODING QUESTIONS:8
#Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)...(until n-x =< 0)
#Test Data:
#sum_series(6) -> 12
#sum_series(10) -> 30


def sum_series(n):
	sum = n
	for i in range(2,n+2,2):
		if (n-i) >= 0: 
			sum = sum + (n-i)
	return(sum)

if __name__ == '__main__':
	a = int(input())
	result = sum_series(a)
	print(result)

#INPUT:
#6

#OUTPUT:
#12