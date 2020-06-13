#You have given a string. You need to remove all the duplicates from the string. 
#The final output string should contain each character only once. The respective order of              the characters inside the string should remain the same. You can only traverse the string at once. 
def dup(str,n):
	index = 0
	for i in range(0,n):
		for j in range(0,i+1):
			if (str[i] == str[j]):
				break
		if(j == i):
			str[index] = str[i]
			index += 1
	return " ".join(str[:index])

str = input()
n = len(str)
p = dup(list(str),n)	
print(p)				
#Input string:  ababacd 
#Output string: abcd
