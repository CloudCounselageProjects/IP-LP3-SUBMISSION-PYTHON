num  = int(input())
sum_series = 0
while(True):
    if(num>=0):
        sum_series = sum_series + num
        num = num - 2
    else:
        break

print(sum_series)