# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:59:27 2020

@author: Sai
"""

def divisor(n1,n2):
    n=0
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            n+=1
    return n        
n1=int(input())
n2=int(input())
print(divisor(n1,n2))            
     