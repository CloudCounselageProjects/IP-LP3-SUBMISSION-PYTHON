# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:26:24 2020

@author: Devanshi
"""

#11
x=input()
my_list=x.split(',')
n=len(my_list)
for i in range(n):
    my_list[i]=int(my_list[i])
print(my_list)
for i in range(n):
    min_ind=i
    for j in range(i+1,n):
        if(my_list[min_ind]>my_list[j]):
            min_ind=j
    my_list[i],my_list[min_ind]=my_list[min_ind],my_list[i]

print(my_list)