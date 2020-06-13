#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Question04
#There are two integers, a and b as input to the program. 
#Output Format: 
#Print the number of common factors of a and b. Both the input value should be in a range of 1 to 10^12.



a = int(input(""))
b = int(input(""))
 
def gcd(a, b):
    if (a == 0): 
        return b; 
    return gcd(b%a, a); 
 
if (a>0 and a<(10**12+1) and b>=1 and b<(10**12+1)):
    count = 1
    for i in range(2, gcd(a, b)+1):
        if a%i==0 and b%i==0:
            count = count+1
    print(count)


# In[ ]:




