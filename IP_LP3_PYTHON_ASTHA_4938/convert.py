file_name = input("Enter filename: ")

#csv_to_tsv fuction

def csv_to_tsv(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read().replace(',', '\t')
            f = open("test.tsv", "w")
            f.write(data)
            f.close()
            print("converted")
    except FileNotFoundError:
        print(file_name + " not found")

#tsv_to_csv fuction

def tsv_to_csv(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read().replace('\t', ',')
            x = open("test.csv", "w")
            x.write(data)
            x.close()
            print("converted")
    except FileNotFoundError:
        print(file_name + " not found")

loop = 'yes'
while loop == 'yes':
    print("1.csv to tsv\n2.tsv to csv")
    option = input("select a option: ")
    if option == '1':
        csv_to_tsv(file_name)
    elif option == '2':
        tsv_to_csv(file_name)
    else:
        print("Invalid option")
        break
    loop = input("enter 'yes' to select option again or 'no' to exit: ")
