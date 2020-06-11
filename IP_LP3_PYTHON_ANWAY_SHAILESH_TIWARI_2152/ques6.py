#question 6

n = input('enter the string:\n')
str1 = n.find('not')
str2 = n.find('poor')
if str2 > str1:
    n = n.replace(n[str1:(str2+4)],'good')
print(n)