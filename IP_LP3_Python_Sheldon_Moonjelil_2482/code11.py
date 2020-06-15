
import datetime
year=int(input("Ënter year in digits: "))
month=int(input("Ënter month in digits: "))
date=int(input("Ënter date in digits: "))
dt = datetime.date(year, month, date) 
wk = dt.isocalendar()[1]
print("week is",wk)