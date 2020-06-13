#Write a Python program to count the number of students of the individual class. 
from collections import Counter
p=int(input("Enter total number of tuples"))
k=[]
for i in range(p):
	b=[]
	classs=input()
	data=int(input())
	b.append(classs)
	b.append(data)
	k.append(tuple(b))

classes=k
Students = Counter(class_name for class_name, no_students in classes)
print(Students)

'''
Sample data: 
classes = ( ('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1), )
'''
#Expected Output: 
#Counter({'VI': 3, '​Example 1:​V': 2, 'VII': 1}) 