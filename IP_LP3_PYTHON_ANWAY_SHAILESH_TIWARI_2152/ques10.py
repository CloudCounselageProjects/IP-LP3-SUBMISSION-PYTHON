# question 11

import datetime
year,month,date = map(int,input().split(','))
print(datetime.date(year,month,date).isocalendar()[1])

