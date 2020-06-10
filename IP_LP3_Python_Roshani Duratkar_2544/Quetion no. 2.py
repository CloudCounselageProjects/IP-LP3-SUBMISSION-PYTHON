# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:13:57 2020

@author: HP
"""

def leap(x):
    if(x%4==0):
        if(x%100==0):
            if(x%400==0):
                return True
            else:
                return False
        else: 
             return True
    else: 
        return False


if __name__ == '__main__': 
    x=int(input("Enter Year:"))
    y=leap(x)
    print(y)

                
          
