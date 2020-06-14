temp=int(input())
op=input(" C for Celsius and F for Fahrenheit")

def C_to_F(temp):
    f=int(((9*temp)/5)+32)
    print("{}°C is {} in Fahrenheit".format(temp,f))

def F_to_C(temp):
    c=int(5*((temp-32)/9))
    print("{}°F is {} in Celsius".format(temp,c))

if(op=='C'):
    C_to_F(temp)

elif(op=='F'):
    F_to_C(temp)
    
