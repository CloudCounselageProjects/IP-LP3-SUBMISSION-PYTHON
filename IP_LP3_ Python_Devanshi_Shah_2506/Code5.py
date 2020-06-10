# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:26:14 2020

@author: Devanshi
"""

#5
from collections import OrderedDict
word=input()
no_rep_word= ("".join(OrderedDict.fromkeys(word))).capitalize()
print(no_rep_word)