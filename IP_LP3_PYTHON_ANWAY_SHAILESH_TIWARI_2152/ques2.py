# question 2

def month(n):
    if n % 400 == 0 or n % 4 == 0 and n % 100 != 0:
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(input('enter the year'))
    y = month(n)
    print(y)