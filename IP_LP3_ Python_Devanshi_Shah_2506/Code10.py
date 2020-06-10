# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:26:23 2020

@author: Devanshi
"""

#10

def BST(root,left,right):
    if((left!=None and left>root) or (right!=None and right<root)):
        return (False)
    else:
        return (True)

my_list=[0]
val=[]
x=input()
list1=x.split(',')
for i in list1:
    my_list.append(int(i))
n=len(my_list)-1
if (n%2==0):
    my_list.append(None)
x=int(n/2)

for i in range(1,x+1):    
    a=my_list[i]
    b=my_list[2*i]
    c=my_list[2*i+1]
    print(a,b,c)
    x=BST(a,b,c)
    val.append(x)
res= all(ele == True for ele in val) 
print(res)