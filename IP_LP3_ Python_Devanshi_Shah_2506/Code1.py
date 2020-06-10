# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:25:58 2020

@author: Devanshi
"""

#1
a=int(input())
b=int(input())
if (a>=1 and a<=10**10) and (b>=1 and b<=10**10):
    print((a+b),(a-b),(a*b))
else:
    print("Enter numbers in the range of 1-10^10")