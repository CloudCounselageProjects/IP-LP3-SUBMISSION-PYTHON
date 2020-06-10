#CODING QUESTIONS:​6 (This code was executed in Visual Studio Code)
#Write a Python program to find the first appearance of the substring 'not' and 'poor' from 
#a given string, if 'not' follows the 'poor', replace the whole 'not'...' poor' substring with'good'.
#Return the resulting string.
# Sample String :  ​'The lyrics is not that poor!' 'The lyrics is poor!' 
# Expected Result :  'The lyrics is good!' 'The lyrics is poor!' 

def good(substr):
  strnot = substr.find("not")
  strpoor = substr.find("poor")
  if strpoor > strnot and strnot>0 and strpoor>0:
    substr = substr.replace(substr[strnot:(strpoor+4)], "good")
    return substr
  else:
    return substr
print(good("The lyrics is not that poor!"))
print(good("The lyrics is poor!"))

#End of question 5