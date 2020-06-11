def leap(yr):
    if(yr%4==0 and yr%400==0 and yr&100!=0):
        return True
    else:
        return False

yr=int(input())
x=leap(yr)
print(x)
