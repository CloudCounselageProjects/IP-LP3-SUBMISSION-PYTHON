'''
Coding Question 11
Write a Python program to get a week number.
Sample Date :
2015, 6, 16
Expected Output :
25
'''
import datetime
l=list(map(int,input().split(',')))
print(datetime.date(l[0],l[1],l[2]).isocalendar()[1])
