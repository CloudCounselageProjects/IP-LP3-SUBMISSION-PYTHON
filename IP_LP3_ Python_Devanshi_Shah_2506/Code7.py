# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:26:18 2020

@author: Devanshi
"""

#7
def func1 (sentence):
    x=sentence.find('not')
    y=sentence.find('poor')
    if(x==-1 or y==-1):
        return(sentence)
    elif(y>x):
        sentence=sentence.replace(sentence[x:y+4],'good')
        return sentence
sent=input()
ans= func1(sent)
print(ans)