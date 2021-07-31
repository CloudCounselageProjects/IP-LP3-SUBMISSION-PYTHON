# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 15:32:57 2021

@author: Pragati
"""

import pandas as pd

df=pd.read_csv("C:\\Users\\Pragati\\Downloads\\AB.csv")
cd=df.to_csv(sep=',')
print(cd)