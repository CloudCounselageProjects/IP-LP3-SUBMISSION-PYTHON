# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:22:27 2020

@author: Sai
"""

def sum_of_series(n):
    i=0
    sum=0
    while n-(2*i)>=0:
        sum=sum+(n-(2*i))
        i+=1
    return sum    


print("sum_of_series(6) -> ",sum_of_series(6))
print("sum_of_series(10) -> ",sum_of_series(10))
