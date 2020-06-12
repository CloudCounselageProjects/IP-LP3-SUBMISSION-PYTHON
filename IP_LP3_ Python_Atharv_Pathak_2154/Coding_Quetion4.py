'''
Problem Statement:

Little Robert likes mathematics. Today his teacher has given him two integers and
asked to find out how many integers can divide both the numbers. Would you like to
help him in completing his school assignment?

'''

def gcd(a, b):                                          #calculate greatest common divisor to improve efficincy

	if (a == 0): 
		return b; 

	return gcd(b%a, a)

a = int(input())
b = int(input())

cnt = 0
for i in range(1, gcd(a, b)+1):
	if a%i==0 and b%i==0:
		cnt=cnt+1
print(cnt)

'''
Output:
10                               #Input
15                               #Input
2                                #Output
'''


