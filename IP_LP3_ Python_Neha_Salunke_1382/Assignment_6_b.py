# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:13:00 2020

@author: Sai
"""

def NotPoor(string1):
    not_pos=string1.find('not')
    poor_pos=string1.find('poor')
    if poor_pos>not_pos and poor_pos>0 and not_pos>0:
        string1=string1.replace(string1[not_pos:(poor_pos+4)],'good')
        return string1
    else:
        return string1
    
string1=input()
print(NotPoor(string1)) 