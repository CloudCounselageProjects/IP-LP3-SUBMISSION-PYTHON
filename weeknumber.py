import datetime
y,m,d=map(int,input().split(","))
date_input=datetime.date(y,m,d)
print(date_input.isocalendar()[1])
