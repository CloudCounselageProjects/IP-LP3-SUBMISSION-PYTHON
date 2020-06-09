# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:21:54 2020

@author: Sai
"""

def select_sort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min=j
        arr[i], arr[min] = arr[min], arr[i]        
    return arr


arr=[14,46,43,27,57,41,45,21,70]
print(select_sort(arr))   