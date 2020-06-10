# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:26:07 2020

@author: Devanshi
"""

#2
def leap_year(x):
    if((x%4==0 and x%100!=0) or (x%400==0)):
        return True
    else:
        return False

y=int(input())
if (y>=1900):
    leap= leap_year(y)
    print(leap)
else:
    print("Enter a year greater than or equal to 1900")