# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:26:09 2020

@author: Devanshi
"""

#3
n=int(input())
words=[]
count={}
length=0
if n>=1 and n<=10**5:
    for i in range(n):
        x=input()
        length+=len(x)
        words.append(x.lower())
else:
    print("enter the value of n between 1 to 10^5")
        
if length<=10**6:
    for word in words:
        if word not in count.keys():
            count[word]=1;
        else:
            count[word]+=1;
else:
    print("The sum of lengths of all the words exceeds 10^6")
    

print(len(count))

for counts in count.values():
    print(counts,end=" ")