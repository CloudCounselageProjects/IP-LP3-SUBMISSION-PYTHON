'''Read two integers from STDIN and print three lines where:
● The first line contains the sum of the two numbers.
● The second line contains the difference between the two numbers (first -
second).
● The third line contains the product of the two numbers.'''



x = int(input())
y = int(input())

if 1<=x<=10**10 and 1<=y<=10**10:
 sum = x+y
 diff = x-y
 prod = x*y

 print (sum)
 print (diff)
 print (prod)