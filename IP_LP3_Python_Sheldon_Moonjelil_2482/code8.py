def sumInt(n):
  if n <= 1:
    return 0
  else:
    return n + sumInt(n - 2)

i=int(input())
print(sumInt(i))
