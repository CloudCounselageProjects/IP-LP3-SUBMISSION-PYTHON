from datetime import date
today = input()
year ,month , day = map(int,today.split(','))

mydate = date(year,month,day)
print(mydate.isocalendar()[1])


