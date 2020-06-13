#Write a Python program to find the first appearance of the substring 'not' and 'poor' from                a given string, if 'not' follows the 'poor', replace the whole 'not'...' poor' substring with 'good'. Return the resulting string
def poor(ip:str)->str:
	NOT = ip.find('not')
	POOR = ip.find('poor')

	if POOR > NOT and NOT > 0 and POOR > 0:
		ip = ip.replace(ip[NOT:(POOR+4)],'good')
		return ip
	else:
		return ip	
	
str1 = input()
str2 = input()
print(poor(str1))
print(poor(str2))

#Sample String :  ​'The lyrics is not that poor!' 
#				  'The lyrics is poor!'
#Expected Result :  'The lyrics is good!'
# 					'The lyrics is poor!' 

