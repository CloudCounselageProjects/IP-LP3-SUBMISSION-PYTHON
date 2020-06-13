#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question03
#You are given n-words. Some words may repeat. For each word, output its number of 
#occurrences. The output order should correspond with the input order of the           
#appearance of the word. See the sample input/output for clarification. 



from collections import OrderedDict
dict = OrderedDict()

for _ in range(int(input())):
    key = input()
    if not key in dict.keys():
        dict.update({key : 1})
    else:
        dict[key] += 1

print(len(dict.keys()))
print(*dict.values())


# In[ ]:




