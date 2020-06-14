def series(n):
  if n < 1:
    return 0
  else:
    return n + series(n - 2)

n=int(input('Enter Number: '))
print('Sum Series of',n,'=',series(n))



"""
OUTPUT:
    
case 1:
Enter Number: 6
Sum Series of 6 = 12

case 2:
Enter Number: 10
Sum Series of 10 = 30

"""
