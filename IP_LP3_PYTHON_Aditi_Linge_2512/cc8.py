n=int(input())
def sum_o(n):
  if n<1:
    return 0
  else:
    return n+sum_o(n - 2)

print(sum_o(n))
