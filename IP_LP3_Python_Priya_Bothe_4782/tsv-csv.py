# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 10:50:30 2021

@author: Admin
"""

import csv

with open("C:\\Users\\Admin\\Desktop\\projecttask\\PB.csv", "r",
          encoding='utf-8') as csv_in, open("C:\\Users\\Admin\\Desktop\\projecttask\\a12.txt", "w",
                                           newline='', encoding='utf-8') as tsv_out:
   csv_in = csv.reader(csv_in)
   tsv_out = csv.writer(tsv_out, delimiter=',')
   
   
   for row in csv_in:
       tsv_out.writerow(row)