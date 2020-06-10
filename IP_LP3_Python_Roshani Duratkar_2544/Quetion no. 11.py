# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:53:57 2020

@author: HP
"""

import datetime
y=int(input("Enter year: "))
m=int(input("Enter month: "))
d=int(input("Enter date: "))
print(datetime.date(y, m, d).isocalendar()[1])
