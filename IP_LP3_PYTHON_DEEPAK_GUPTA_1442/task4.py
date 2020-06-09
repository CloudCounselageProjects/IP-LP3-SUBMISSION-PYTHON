number_1 = int(input().strip())
number_2 = int(input().strip())
count = 0
for i in range(1, min(number_1, number_2)+1):
    if number_1 % i == 0 and number_2 % i == 0:
        count += 1
print(count)
