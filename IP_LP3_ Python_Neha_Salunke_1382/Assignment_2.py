# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:48:38 2020

@author: Sai
"""

def LeapYear(y):
    if(y%4==0 and y%100!=0   or y%400==0):
        return True
    else:
        return False
y=int(input())
print(LeapYear(y))