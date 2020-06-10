# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:26:12 2020

@author: Devanshi
"""

#4
a=int(input())
b=int(input())
small=min(a,b)
count=0
for i in range (1,small+1):
    if(a%i==0 and b%i==0):
        count+=1
print(count)