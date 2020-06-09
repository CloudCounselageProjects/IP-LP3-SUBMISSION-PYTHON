# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:12:02 2020

@author: Sai
"""

import datetime
date=input().strip().split(",")
print(datetime.date(int(date[0]),int(date[1]),int(date[2])).isocalendar()[1])