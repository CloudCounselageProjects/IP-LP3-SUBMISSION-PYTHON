def leap(a):
        if 1900<=a<=10**10:
                if(a%4==0 and a%400==0 and a&100!=0):
                        return True
                else:
                        return False
year=int(input())
x=leap(year)
print(x)
