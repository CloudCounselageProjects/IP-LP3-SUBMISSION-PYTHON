import re
temp=input()
temp1=temp[0:-1]
x=re.search("[c,C]",temp)
if(x):
    f=int(round(int(temp1)*(9/5)+32))
    print("{}°C is {} in Fahrenheit".format(temp1,f))
else:
    c=int(round((int(temp1)-32)*5/9))
    print("{}°F is {} in Celsius".format(temp1,c))
