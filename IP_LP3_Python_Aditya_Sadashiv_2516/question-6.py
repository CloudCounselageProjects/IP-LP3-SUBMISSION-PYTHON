import re
str1=input()
notn=str1.find('not')
poorn=str1.find('poor')
if (poorn>notn and (poorn>0 and notn>0)):
    str2=re.sub(str1[notn:poorn+4],"good",str1)
    print(str2)
else:
    print(str1)
