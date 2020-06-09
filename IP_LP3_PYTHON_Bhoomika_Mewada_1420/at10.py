#CODING QUESTIONS:11
#Write a Python program to get a week number.
import datetime
year,month,date=map(int,input().split(","))
print(datetime.date(year,month,date).isocalendar()[1])