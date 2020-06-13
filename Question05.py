#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question05You have given a string. You need to remove all the duplicates from the string. 
#The final output string should contain each character only once. The respective order of 
#the characters inside the string should remain the same. You can only traverse the
#string at once



a=str(input())
b=set()
for x in a:
    if x not in b:
        b.add(x)
        print(x,end="")


# In[ ]:




