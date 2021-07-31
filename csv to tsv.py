# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 15:31:06 2021

@author: Pragati
"""

import pandas as pd

df=pd.read_csv("C:\\Users\\Pragati\\Downloads\\CSV\\av.csv")
cd=df.to_csv(sep='\t')
print(cd)