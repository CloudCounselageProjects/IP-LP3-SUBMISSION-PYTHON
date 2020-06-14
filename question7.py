def celtofahren(temp):
    return round(((temp/5)*9)+32)
def fahrentocel(temp):
    return round(((temp-32)/9)*5)
print("enter the temperature")
temp=int(input())
print("enter 1 to convert from celsius to fahrenheit")
print("enter 2 to convert from fahrenheit to celsius")
i=int(input())
if i==1:
    print(temp,chr(176),'c is ',celtofahren(temp),' in Fahrenheit',sep='')
elif i==2:
    print(temp,chr(176),'F is ',fahrentocel(temp),' in Celsius',sep='')
else:
    print("wrong key entered! try again")