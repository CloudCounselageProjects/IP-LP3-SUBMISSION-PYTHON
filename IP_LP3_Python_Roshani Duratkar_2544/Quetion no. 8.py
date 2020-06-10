# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:28:57 2020

@author: HP
"""

def sum_series(n):
  if n < 1:
    return 0
  else:
    return n + sum_series(n - 2)

n=int(input("Enter no.:"))
print(sum_series(n))

