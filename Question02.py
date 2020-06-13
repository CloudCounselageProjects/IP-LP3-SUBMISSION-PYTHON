#!/usr/bin/env python
# coding: utf-8

# In[7]:


#QUESTION02
#You are given the year, and you have to write a function to check if the year is a leap or not. 
#Input Format Read y, the year that needs to be checked. 
#Constraints 1900<_y<_10 
#Output Format The output is taken care of by the template.
#Your function must return a boolean value (True/False


year = int(input())
x ="True"
if(year%100==0):
    x ="False"
    if(year%400==0):
        x ="True"
elif(year%4==0):
    x="True"

print(x)


# In[ ]:





# In[ ]:




