#CODING QUESTIONS:12
#Write a Python program to count the number of students of the individual class.
n=int(input("No of inputs:"))
l=[]
s=[]
for i in range(n):
    V=list(input().split())
    l.append(V[1])
    s.append(V[0])
j=set(s)
for i in j:
    print(i,s.count(i))
#hua