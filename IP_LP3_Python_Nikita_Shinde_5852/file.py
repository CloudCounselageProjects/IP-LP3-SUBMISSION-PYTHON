#To convert Both given file from tsv to csv and vice-versa
import csv
import pandas as pd
while True:
  inp_file = input("Enter The name of your .csv file and .tsv file for Conversion \n Else Enter Q to Quit  ").lower()
  if inp_file == 'q':
    quit()
  csv_file,tsv_file= list(inp_file.split(" "))
  if '.csv' in csv_file and '.tsv' in tsv_file:
    with open (csv_file,'r') as f:
      csv_reader = csv.reader(f)
      with open('Converted.tsv','w') as f1:
        csv_writer = csv.writer(f1, delimiter = '\t')
        for line in csv_reader:
          csv_writer.writerow(line)

    csv_table=pd.read_table(tsv_file,sep='\t')
    csv_table.to_csv('Converted.csv',index=False)
  raise IOError("InvalidFileTypeException")
  
  


  

