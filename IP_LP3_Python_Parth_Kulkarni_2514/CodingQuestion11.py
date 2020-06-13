#Write a Python program to get a week number.
from datetime import date
year,month,date1 = map(int,input().split(","))
Date = date(year,month,date1)
weeknum = Date.isocalendar()[1]  
print(weeknum)
#Sample Date : 2015, 6, 16 
#Expected Output :  25 