#1
a = int(input(" "))
b = int(input(" "))
print(a+b,a-b,a*b)  
  
#2
a = int(input(" "))
if a%4==0 & a%100==0 & a%400==0:
    print("True")
else:
    print("False")

#3
from collections import Counter,OrderedDict
class OrderedCounter(Counter,OrderedDict):
    pass
d=OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())
'''from collections import OrderedDict
def check():
    list=OrderedDict()
    num=int(input())
    for _ in range(num):
        word=''.join(input().lstrip().rstrip().split(' '))
        list[word]=list.get(word,0)+1
    print(len(list))
    for item in list.values():
        print(item,end=' ')
    return 0'''
    
#4
a=int(input(" "))
b=int(input(" "))
def gcd(a,b):
    if (a==0):
        return b
    return gcd(b%a, a)
count=0    
for i in range(1,gcd(a,b)+1):
    if a%i==b%i==0:
       count=count+1
print(count)
    

#5
x=str(input(" "))
final="".join(dict.fromkeys(x))
print(final)


#6.1
import math
import os
import random
import re
import sys
 
# Complete the countSpecialElements function below.
 
def countSpecialElements(matrix):
  nRows= len(matrix)
  nCount=0
 
  for row in matrix:
    for indexCol, element in enumerate(row):
 
      if element==min(row) or element==max(row):
        if row.count(element)>1:
          return -1
        nCount=nCount+1
 
      else:
        listColumn=[]
 
        for indexRow in range(0, nRows):
          listColumn.append(matrix[indexRow][indexCol])
 
        if element==min(listColumn) or element==max(listColumn):
          if listColumn.count(element)>1:
            return -1
          nCount=nCount+1
 
  return nCount


#R = int(input("Enter the number of rows:"))
#C = int(input("Enter the number of columns:"))
 
# Initialize matrix
def slicing(a,step):
    return [a[i::step] for i in range(step)]
#print(slicing(a,3))

matrixx = []
print("Enter the entries rowwise:")
 
# For user input
a=[]
for i in range(3):          # A for loop for row entries
    #a =[]
    for j in range(3):      # A for loop for column entries
        a.append(int(input()))
    matrixx.append(a)
mat=slicing(a,3)
print(mat)
#print(slicing(a,3))

if __name__ == '__main__':
  nCount = countSpecialElements(mat)
  print(nCount)



# A basic code for matrix input from user
 

             

'''
# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrixx[i][j], end = " ")
   # print()
'''
#6.2
a=str(input(" "))
a1=str(input(" "))
x=a.replace("not that poor","good")
print(x)
print(a1)

#7
c=int(input("enter celcius: "))
f=((9*c)/5)+32
f3=int(f)                                            
print(c,"C is",f3,"in Fahreheit")
f1=int(input("enter fahreheit: "))
c1=((f1-32)*5)/9
c2=int(c1)
print(f1,"F is",c2,"in Celsius")

#8
def func8(a):
    if a<1:
        return 0
    else:
        return a+func8(a-2)
a=int(input("enter no: "))
print(func8(a))
#9
INT_MAX = 4294967296
INT_MIN = -4294967296
  
 
class Node: 
  
 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
  
 
def isBST(node): 
    return (isBSTUtil(node, INT_MIN, INT_MAX)) 
  
 
def isBSTUtil(node, mini, maxi): 
      
 
    if node is None: 
        return True
  
 
    if node.data < mini or node.data > maxi: 
        return False
 
    return (isBSTUtil(node.left, mini, node.data -1) and
          isBSTUtil(node.right, node.data+1, maxi)) 
a=int(input(" "))
b=int(input(" "))
c=int(input(" "))
root = Node(a) 
root.left = Node(b) 
root.right = Node(c)

if (isBST(root)): 
    print ("true")
else: 
    print ("false")
    
     
#10    
a =[]
n = int(input("enter number of element to sort: "))
for i in range(0,n):
    item=int(input())
    a.append(item)
print(" ",a)
a.sort()
print(a)
    
#11
import datetime
x=int(input("enter year: "))
y=int(input("enter month: "))
z=int(input("enter day: "))
print(datetime.date(x,y,z).isocalendar()[1])

#12 
from collections import Counter
classes={}
x=int(input("enter no class and students in class:  "))
for i in range(x):
    a=input("enter class name: ")
    b=input("enter students: ")
    classes[a]=b

students = Counter(classes)
print(students) 


#from collections import Counter
#classes = (('V', 1),('VI', 1),('V', 2),('VI', 2),('VI', 3),('VII', 1))
#students = Counter(class_name for class_name, no_students in classes)
#print(students)  