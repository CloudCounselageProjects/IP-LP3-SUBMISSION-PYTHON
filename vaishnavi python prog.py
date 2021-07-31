import csv

answer = input("Enter 'tsv' to convert from  csv to tsv and 'csv' for tsv to csv : ")
if answer == 'tsv':
    file1 = input("CSV file: ")
    result1 = input("Path to save: ")
    with open(file1, 'r') as csv_in:
        csv_in = csv.reader(csv_in, delimiter=',')
        tsv_out = open(result1, 'w')
        result1 = csv.writer(tsv_out, delimiter='\t')
        result1.writerows(csv_in)
elif answer == 'csv':
    file2 = input("TSV file: ")
    result2 = input("Path to save: ")
    with open(file2, 'r') as tsv_in:
        tsv_in = csv.reader(tsv_in, delimiter='\t')
        csv_out = open(result2, 'w')
        result2 = csv.writer(csv_out, delimiter=',')
        result2.writerows(tsv_in)

else:
    print("INVALID")
