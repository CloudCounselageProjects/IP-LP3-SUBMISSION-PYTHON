#question 4


n = int(input('enter 1st the no\n'))
m = int(input('enter the 2nd no\n'))
c = 0
k=1
while k < n and k < m:
    if n % k == 0 and m % k == 0:
        c += 1
    k += 1

print(f'common factor of {n} and {m} is ', c)