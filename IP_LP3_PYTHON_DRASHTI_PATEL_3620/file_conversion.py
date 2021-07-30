import pandas as pd
import csv

print("Enter\n1---> csv to tsv\n2---> tsv to csv\n")
a=int(input())
if a==1:
    print("Converting csv to tsv")
    p=input("Enter complete file path:[including file name] \n")
    sp=input("Enter complete path to save your file: [with name of new file at the end] \n")

    print("tsv file will be available here\n",sp)

    with open(p,'r') as csvin, open(sp, 'w') as tsvout:
        csvin = csv.reader(csvin)
        tsvout = csv.writer(tsvout, delimiter='\t')

        for row in csvin:
            tsvout.writerow(row)

    with open(sp, newline='') as f:
        print("Resulting file")
        reader = csv.reader(f)
        row1 = next(reader)
        print(row1)

    if a==2:
        print(" converting tsv to csv")
        p=input("Enter complete file path: \n")

        with open(p,'r') as fin:
            cr = csv.reader(fin, delimiter='\t')
            filecontents = [line for line in cr]
        with open(sp,'w') as fout:
            cw = csv.writer(fout, quotechar='', quoting=csv.QUOTE_NONE, escapechar='\\')
            cw.writerows(filecontents)

        
        with open(sp, newline='') as f:
            print("Resulting file")
            reader = csv.reader(f)
            row1 = next(reader)
            print(row1)

