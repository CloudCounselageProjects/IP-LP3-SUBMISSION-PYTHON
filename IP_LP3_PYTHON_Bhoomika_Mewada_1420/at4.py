"""
CODING QUESTIONS:4
Little Robert likes mathematics. Today his teacher has given him two integers and
asked to find out how many integers can divide both the numbers. Would you like to
help him in completing his school assignment?
"""

#Two integers given as input
n1=int(input())
n2=int(input())
#to count no of factors
count=0
for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        count+=1
print(count)
