#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Question09
#Write a Python program to get a week number.  

import datetime
l=list(map(int,input().split(',')))
print(datetime.date(l[0],l[1],l[2]).isocalendar()[1])


# In[ ]:




