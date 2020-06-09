# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:12:00 2020

@author: Sai
"""

any_string=input()
result=''.join(dict.fromkeys(any_string))
print(result)