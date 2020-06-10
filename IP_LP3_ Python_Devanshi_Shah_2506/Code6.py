# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:26:16 2020

@author: Devanshi
"""
#6
import numpy as np
k=1
while k>0:
    m=int(input())
    n=int(input())
    if((m>0 and m<100) and (n>0 and n<100)):
        break
    else:
        print("enter m and n between 0-100")
    

nums=[]
i=1
while i<(m*n+1):
    x=int(input())
    if(x not in nums and x>-1):
        nums.append(x)
    else:
        print("enter distinct and positive numbers")
        i=i-1
    i+=1
matrix=np.array(nums).reshape(m,n)
print(matrix)

rowmax=[]
rowmin=[]
colmax=[]
colmin=[]

for i in range (m):
    rmin=60000
    rmax=-1
    for j in range(n):
        if(matrix[i][j]> rmax):
            rmax=matrix[i][j]
        if(matrix[i][j]<rmin):
            rmin=matrix[i][j]
    rowmax.append(rmax)
    rowmin.append(rmin)
    
for j in range (n):
    cmin=60000
    cmax=-1
    for i in range(m):
        if(matrix[i][j]> cmax):
            cmax=matrix[i][j]
        if(matrix[i][j]<cmin):
            cmin=matrix[i][j]
    colmax.append(cmax)
    colmin.append(cmin)
    

count=0
for i in range(m):
    for j in range(n):
        if((matrix[i][j]==rowmax[i])|(matrix[i][j]==rowmin[i])|(matrix[i][j]==colmax[j])|(matrix[i][j]==colmin[j])):
            count+=1
print()
print(count)