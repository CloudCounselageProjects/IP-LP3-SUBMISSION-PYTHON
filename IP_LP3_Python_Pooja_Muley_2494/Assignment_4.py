'''Little Robert likes mathematics. Today his teacher has given him two integers and
asked to find out how many integers can divide both the numbers. Would you like to
help him in completing his school assignment?
'''


a = int(input())
b = int(input())
n = 0
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        n = n + 1
print(n)