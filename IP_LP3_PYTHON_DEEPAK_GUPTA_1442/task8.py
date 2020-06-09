
ans = 0
pos_integer = int(input().strip())
for i in range(0, pos_integer+1, 2):
    if pos_integer - i > 0:
        ans += pos_integer - i
print(ans)
