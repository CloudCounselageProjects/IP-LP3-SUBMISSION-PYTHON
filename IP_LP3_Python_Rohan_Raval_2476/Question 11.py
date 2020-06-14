import datetime
s=input('Enter year, month, date: ')
year,month,day=map(int,s.split(','))
a_date = datetime.date(year,month,day)
week_number = a_date.isocalendar()[1]
print('Week Number =',week_number)



"""
OUTPUT:
    
Enter year, month, date: 2015,6,16
Week Number = 25

"""