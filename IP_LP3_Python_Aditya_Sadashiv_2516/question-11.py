import datetime
year,month,day=map(int,input().split(","))
date_input=datetime.date(year,month,day)

print(date_input.isocalendar()[1])
