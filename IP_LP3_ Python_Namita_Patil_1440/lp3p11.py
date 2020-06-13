#CODING QUESTIONS:11
#Write a Python program to get a week number.
#Sample Date :
# 2015, 6, 16
#Expected Output :
#25



import datetime
date = input().split(', ')
y = date[0]
m = date[1]
d = date[2]
week_number = datetime.date(int(y), int(m), int(d)).isocalendar()[1]
print(week_number)

#INPUT:
#2015, 6, 16

#OUTPUT:
#25