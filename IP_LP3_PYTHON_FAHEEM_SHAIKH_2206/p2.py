print('Enter the year to check whether the year is leap year or not: ')
year = int(input())

if (year%400 == 0):
          print("True")
elif (year%100 == 0):
          print("False")
elif (year%4 == 0):
          print("True")
else:
          print("False")
