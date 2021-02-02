import datetime
year,month,date=map(int,input().split(','))
date_input=datetime.date(year,month,date)
print(date_input.isocalendar()[1])