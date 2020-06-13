#Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... 
def sum_series(n):
	if n < 1:
		return 0
	else:
		return n + sum_series(n-2)

n = int(input())
p = sum_series(n)
print(p)		
#Test Data: sum_series(6) -> 12 
#			sum_series(10) -> 30 	