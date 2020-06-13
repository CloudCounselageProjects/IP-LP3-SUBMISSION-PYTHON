from datetime import date

date_str = input()

y,m,d = map(int,date_str.split(","))

date1 = date(y,m,d)
date2 = date(y,1,1)

day = date1 - date2

print(day.days)

print(int(day.days/7))

date1.isocalendar()[1]




