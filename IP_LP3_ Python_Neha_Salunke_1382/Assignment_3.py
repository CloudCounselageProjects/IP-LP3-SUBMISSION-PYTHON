# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:53:26 2020

@author: Sai
"""

from collections import OrderedDict
words = OrderedDict()

for _ in range(int(input())):
    word = input()
    words.setdefault(word, 0)
    words[word] += 1
   
print(len(words))
print(*words.values())