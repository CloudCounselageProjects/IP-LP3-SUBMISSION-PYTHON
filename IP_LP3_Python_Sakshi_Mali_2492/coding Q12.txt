#coding question 12
import datetime
print("enter date in sequence:year,month,day")
yyyy=int(input())
mm=int(input())
dd=int(input())
print(datetime.date(yyyy, mm, dd).isocalendar()[1])
