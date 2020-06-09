#QUES 2

def leap_year(year):
    
    leap=False
    
    if year%400==0:
        return True
    elif year%100==0:
        return leap
    elif year%4==0:
        return True
        
     
    return leap
year = int(input())
print(leap_year(year))