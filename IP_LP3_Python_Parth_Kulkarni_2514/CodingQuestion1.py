#Read two integers from STDIN and print three lines where: ● The first line contains the sum of the two numbers. ● The second line contains the difference between the two numbers (first - second). ● The third line contains the product of the two numbers. 
a, b = input().split()
c = int(a) + int(b)
d = int(a) - int(b)
e = int(a) * int(b)
print(int(c),int(d),int(e))
#Sample Input 3    2 
#Sample Output  5  1   6 
