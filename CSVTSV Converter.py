# -*- coding: utf-8 -*-
"""
Edited by Mayur Yerawar

Code to convert CSV file to TSV and vice versa
"""

import pandas as pd

csv_path_read = input("Enter the path of csv file to convert : \n")
tsv_path_read = input("Enter the path of tsv file to convert :\n") 

if ((tsv_path_read == "NA") & (csv_path_read == "NA") ) :
    print("Please enter the correct path")
    
elif ((tsv_path_read == "NA") & (csv_path_read != "NA")):
    path_to_write = input("Enter the path to save the file : \n")    
    csv_read = pd.read_csv(csv_path_read)
    with open(path_to_write,'w') as write_tsv:    
        write_tsv.write(csv_read.to_csv(sep='\t', index=False))
    if path_to_write == "NA":
        print("Please enter correct destination path")
    else:
        print("\nFile successfully converted to tsv\n"+"Please refer below path for output : \n"+path_to_write)

elif ((csv_path_read == "NA") & (tsv_path_read != "NA")):
   path_to_write = input("Enter the path to save the file : \n")    
   tsv_read = pd.read_csv(tsv_path_read, sep='\t')   
   with open(path_to_write,'w') as write_csv:
       write_csv.write(tsv_read.to_csv(sep=',', index=False))
   if path_to_write == "NA":       
       print("Please enter correct destination path")
   else:       
       print("\nFile successfully converted to csv\n"+" Please refer below path for output : \n"+path_to_write)
    

    



 
