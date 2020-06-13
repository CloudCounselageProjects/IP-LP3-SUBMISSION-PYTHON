#CODING QUESTIONS:5
#You have given a string. You need to remove all the duplicates from the string. The final output string should contain each character only once. The respective order of the characters inside the string should remain the same. You can only traverse the
#string at once.
#Input string:
#ababacd
#Output string:
#Abcd

def sort(b):
	final = ''.join(sorted(set(b),key = b.index))
	c = final.capitalize()
	return (c)

a = input()
result = sort(a)
print(result)

#INPUT:
#ababacd

#OUTPUT:
#ababacd
