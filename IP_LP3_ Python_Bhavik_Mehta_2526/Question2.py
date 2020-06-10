def is_leap(year):
    leap = 'It is not a Leap year'
    if year % 400 == 0:
        leap = 'It is a Leap year'
    elif year % 100 == 0:
        leap = 'It is not a Leap year'
    elif year % 4 == 0:
        leap = 'It is a Leap year'
    return leap
year = int(input())
print(is_leap(year))