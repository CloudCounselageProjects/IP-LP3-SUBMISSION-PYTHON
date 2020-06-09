"""
CODING QUESTIONS:7
Write a Python program to convert temperatures to and from celsius, Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in
Fahrenheit ]
"""
#Write a Python program to convert temperatures to and from celsius, Fahrenheit
s=input()
if s[-1].upper()=="C":
    f=(9*(int(s[:-2]))//5)+32
    print(s,"is",f,"in Fahrenheit")
if s[-1].upper()=="F":
    c=(5*(int(s[:-2])-32))//9
    print(s ,"is",c,"in Celsius")