'''
Coding Question 7
Write a Python program to convert temperatures to and from celsius, Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in
Fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
'''
def c_f(a,s):
    c1=0
    if(s==1):
        c1=float((a-32)*(5/9))
        return int(c1)
    else:
        c1=float((9/5)*(c)+32)
        return int(c1)
c=int(input("Enter celsius to convert : "))
print(c,"°C is",c_f(c,0),"in Fahrenheit")
f=int(input("Enter fahrenheit to conver: "))
print(f,"°F is",c_f(f,1),"in Celsius")
