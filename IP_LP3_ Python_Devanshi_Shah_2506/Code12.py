# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:11:39 2020

@author: Devanshi
"""

#12
import datetime as dt
date=input()
date_list=(date.split(','))
y=int(date_list[0])
m=int(date_list[1])
d=int(date_list[2])
date=dt.date(y,m,d)
weeknum=(date.isocalendar())[1]
print(weeknum)