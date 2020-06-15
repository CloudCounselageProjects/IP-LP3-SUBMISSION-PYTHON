


def isLeap(y):
    if y%4==0:
        return True
    if y%100==0:
        return True
    if y%400==0:
        return True
    return False
print(isLeap(int(input())))
