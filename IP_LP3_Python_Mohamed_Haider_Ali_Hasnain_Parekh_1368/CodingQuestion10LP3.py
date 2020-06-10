#CODING QUESTIONS:​12 (This code was executed in Visual Studio Code)
#Write a Python program to count the number of students of the individual class.  
#Sample data: 
#classes = ( ('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1), )
#Expected Output: Counter({'VI': 3, '​Example 1:​V': 2, 'VII': 1})


from collections import Counter                     #Import counter (A counter allows you to count the items and can be used on string, tuple, list)
Classes = (
     ('V', 1),
     ('VI', 1),
     ('V', 2),
     ('VI', 2),
     ('VI', 3),
     ('VII', 1),
     )
Student = Counter(Class_name for Class_name, num_Student in Classes)
print (Student)

#End of question 10

