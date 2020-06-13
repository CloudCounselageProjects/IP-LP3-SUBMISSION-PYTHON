#CODING QUESTIONS:6
#Write a Python program to find the first appearance of the substring 'not' and 'poor' from
#a given string, if 'not' follows the 'poor', replace the whole 'not'...' poor' substring with
#'good'. Return the resulting string.
#Sample String :
#'The lyrics is not that poor!'
#'The lyrics is poor!'
#Expected Result :
#'The lyrics is good!'
#'The lyrics is poor!'

str1 = input()
str_not = str1.find('not')
str_poor = str1.find('poor')
if(str_not < str_poor and str_not > 0):
	str1 = str1.replace(str1[str_not:(str_poor+4)], 'good')
	print(str1)
else:
	print(str1)

#INPUT:
#The lyrics is not that poor!

#OUTPUT:
#The lyrics is good!
