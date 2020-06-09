def is_leap(n):
    leap = False

    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            return False
        return True
    else:
        return False

    return leap


year = int(input())
print(is_leap(year))