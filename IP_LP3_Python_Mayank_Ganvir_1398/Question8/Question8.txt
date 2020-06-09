def series(n):
    if n<1:
        return 0
    else:
        return n+series(n-2)
print(series(10))