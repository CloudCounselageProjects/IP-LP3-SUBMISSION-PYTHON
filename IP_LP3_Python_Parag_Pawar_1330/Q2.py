a = int(input())

def Leapyear() :
    if ((a%4==0) and (a%100==0)): 
        flag = True
    else :
        flag = False
    if ((flag==True) and (a%400==0)):
        flag = True
    else :
        flag = False
    return flag
print(Leapyear())

      
