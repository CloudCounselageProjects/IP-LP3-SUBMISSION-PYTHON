#CODING QUESTIONS:​11 (This code was executed in Visual Studio Code)
#Write a Python program to get a week number.
#Sample Date : 2015, 6, 16
# Expected Output : 25  


import datetime
weeknum = datetime.date(2015,6,16).isocalendar()[1]
print ('The week number is : ', weeknum)

#End of question 9