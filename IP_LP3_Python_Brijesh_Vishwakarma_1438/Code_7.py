print("for celsius to fahreneit type 1")
print("for fahreneit to celsius type 2")
n=int(input())
t=int(input())
if (n==1):
    result=int((t*(9/5))+32)
    print(t,"°C is ",result,"in fahreneit")
else:
    result=int((t-32)*5/9)
    print(t,"°F is",result,"in celsius")