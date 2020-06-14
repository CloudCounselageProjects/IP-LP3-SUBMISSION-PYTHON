def findpoor(str1):
  not = str1.find('not')
  poor = str1.find('poor')
  if poor>not and not>0 and poor>0:
    str1 = str1.replace(str1[not:(poor+4)], 'good')
  return str1
print(findpoor('The lyrics is not that poor!'))
print(findpoor('The lyrics is poor!'))