#CODING QUESTIONS:4
#Little Robert likes mathematics. Today his teacher has given him two integers and asked to find out how many integers can divide both the numbers. Would you like to help him in completing his school assignment?
#Input Format :
#There are two integers, a and b as input to the program.
#Output Format:
# Print the number of common factors of a and b. Both the input value should be in a
#range of 1 to 10^12.
#Input:
#10
#15
#Output:
#2

count = 1
a = int(input())
b= int(input())
n = a if a > b else b
for i in range(2,n+1):
	if(a % i == 0 and b % i == 0):
		count = count + 1
print(count)

#INPUT:
#10
#15

#OUTPUT:
#2