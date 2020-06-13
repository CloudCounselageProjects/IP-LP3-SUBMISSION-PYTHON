#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question10
#Write a Python program to count the number of students of the individual class. 



from collections import Counter
classes={}
x=int(input("enter no class and students in class:  "))
for i in range(x):
    a=input("enter class name: ")
    b=input("enter students: ")
    classes[a]=b

students = Counter(classes)
print(students)


# 
