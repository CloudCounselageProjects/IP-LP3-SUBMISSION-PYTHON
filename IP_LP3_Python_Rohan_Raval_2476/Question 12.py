
from collections import Counter
classes={}
x=int(input("Enter Number of classes:  "))
for i in range(x):
    a=input("Enter Class: ")
    b=input("Enter Number of students: ")
    classes[a]=b

students = Counter(classes)
print(students) 




"""
OUTPUT:
    
Enter Number of classes:  3

Enter Class: V

Enter Number of students: 6

Enter Class: VI

Enter Number of students: 4

Enter Class: VIII

Enter Number of students: 9
Counter({'VIII': '9', 'V': '6', 'VI': '4'})

"""