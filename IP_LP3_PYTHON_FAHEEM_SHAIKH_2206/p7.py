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
f=int(input("Enter fahrenheit to convert: "))
print(f,"°F is",c_f(f,1),"in Celsius")
