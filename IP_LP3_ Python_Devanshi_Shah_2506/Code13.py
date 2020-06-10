# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:48:12 2020

@author: Devanshi
"""

#13
from collections import Counter
n=int(input())
classes=[]
for r in range(n):
    x=input()
    classes.append((x.split(',')[0],int(x.split(',')[1])))
     
"""
The input is to be entered as
6
V,1
VI,1
V,2
VI,2
VI,3
VII,1
"""
students = Counter(class_name for class_name, number in classes)
print(students)


    



    



        
        
    
 




    
    
   