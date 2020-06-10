# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:26:22 2020

@author: Devanshi
"""

#9
def sum_series(n):
    i=n
    sum=0
    while i>=0:
        sum=sum+i
        i=i-2
    print(sum)


i=1
while i>0:
    x=int(input())
    if(x<0):
        print("Enter a positive number")
    else:
        break
sum_series(x)