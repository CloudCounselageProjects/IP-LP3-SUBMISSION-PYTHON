import re
str1=input()
n=str1.find('not')
p=str1.find('poor')
if (p>n and (p>0 and n>0)):
    str2=re.sub(str1[n:p+4],"good",str1)
    print(str2)
else:
    print(str1)
