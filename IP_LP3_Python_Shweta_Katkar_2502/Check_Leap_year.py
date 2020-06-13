def CheckLeapYear(y):
    if y%4==0:
        res = True
    elif y%100==0:
        res = True
    elif y%400==0:
        return True
    else:
        res = False
    return(res)


    


y=int(input("Enter year: "))
a=CheckLeapYear(y)
print(a)  
    
