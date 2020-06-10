# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:11:43 2020

@author: HP
"""

a = int(input("Enter 1st no.:"))
b = int(input("Enter 2nd no.:"))
n = 0
  
for i in range(1, min(a, b)+1): 
    if a%i==b%i==0: 
        n+=1
      
print(n) 
