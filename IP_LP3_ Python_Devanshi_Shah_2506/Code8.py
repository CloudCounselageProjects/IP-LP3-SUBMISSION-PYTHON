# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:26:21 2020

@author: Devanshi
"""

#8

temp=input()
degree=int("".join(filter(str.isdigit,temp)))
cf=temp[-1]
if cf.upper()=='C':
    result = int(round((9 * degree) / 5 + 32))
    print("{}°C is {} in Fahrenheit".format(degree,result)) 
elif cf.upper()=='F':
    result = int(round((degree - 32) * 5 / 9))
    print("{}°F is {} in Celsius".format(degree,result))
else:
    print("enter values as 45c or 45f")