def leap(y):
    leap=False
    if y % 400 == 0 or y % 4==0:
        return True
    elif y % 100 == 0:
        return False
    return leap

print(leap(int(input())))



"""
OUTPUT:
    
case 1:
1990
False

case 2:
2016
True

"""