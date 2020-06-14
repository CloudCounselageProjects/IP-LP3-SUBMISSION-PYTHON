import datetime
year,month,day=int(input()),int(input()),int(input())
print(datetime.date(year,month,day).isocalendar()[1])