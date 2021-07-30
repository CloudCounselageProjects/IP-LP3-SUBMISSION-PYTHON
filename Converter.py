import pandas as pd
import os

print(" FILE CONVERSION ")
while True:
    print(" 1) Convert csv to tsv ")
    print(" 2) Convert tsv to csv ")
    print(" 3) Exit \n")
    choice = int(input(" Enter your choice: "))
    if choice == 1:
        csv_file = input("Enter path to csv file: ")
        if os.path.exists(csv_file):
            tsv_result = input("Enter path to save the conversion: ")
            csv_read = pd.read_csv(csv_file)
            with open(tsv_result, 'w') as write_tsv:
                write_tsv.write(csv_read.to_csv(sep='\t', index=False))
            print("\n Conversion completed, follow the path to view tsv file:  " "'" + tsv_result + "'\n")
        else:
            print(" Please enter correct path! ")
    elif choice == 2:
        tsv_file = input("Enter path to tsv file: ")
        if os.path.exists(tsv_file):
            csv_result = input("Enter path to save the conversion: ")
            tsv_read = pd.read_csv(tsv_file, sep='\t')
            with open(csv_result, 'w') as write_csv:
                write_csv.write(tsv_read.to_csv(sep=',', index=False))
            print("Conversion completed, follow the path to view csv file " + csv_result)
        else:
            print(" Please enter correct path! ")
    elif choice == 3:
        break
    else:
        print(" Wrong input! ")
