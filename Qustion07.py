#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question07
#Write a Python program to convert temperatures to and from celsius, Fahrenheit.


print("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius")
x=int(input("Select from options:\t"))

if x==1:
    c=int(input("Enter temperature in Celsius:\t"))
    f=(c*9/5)+32
    print(c, " °C is ", round(f) ," in Fahrenheit " )
elif x==2:
    f=int(input("Enter temperature in Fahrenheit:\t"))
    c=(f-32)*5/9
    print(f, " °F is ",round(c)," in Celsius ")
else:
 print("Select between 1 or 2")


# In[ ]:





# In[ ]:




