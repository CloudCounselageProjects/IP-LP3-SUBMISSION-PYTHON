# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:08:30 2020

@author: HP
"""




e=1
while(e==1):
    print("1:celsius to Fahrenheit.\n2:Fahrenheit to celsius")
    ch=int(input("Enter choice: "))
    x=int(input("Enter temparature: "))
    
    if (ch==1):
        f= (x*9/5)+32
        print(f)
    elif(ch==2):
        c = (x-32)*5/9
        print(c)
    e=int(input("prees 1 to contonue and 0 to quit:"))