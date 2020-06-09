# 2
def is_leap_year(year):
    """
    Returns whether the given Gregorian year is a leap year.
    """
    return ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0))


year = int(input())
print(is_leap_year(year))
