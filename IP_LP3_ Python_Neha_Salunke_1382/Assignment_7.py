# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:16:00 2020

@author: Sai
"""

def CelsiusToFahren(c):
    return int((9/5)*c+32)
def FahrenToCelsius(f):
    return int((5/9)*(f-32))
    
print("1.Celsius to Fahrenheit\n2.Fahrenheit to Celsius")
choice=int(input("Enter choice :"))
value=int(input("Enter value :"))
if choice==1:
    print(value,"°C is",CelsiusToFahren(value),"in Fahrenheit" )
else:
    print(value,"°F is",FahrenToCelsius(value),"in Celsius")