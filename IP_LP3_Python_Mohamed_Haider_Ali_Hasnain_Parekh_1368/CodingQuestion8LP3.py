#CODING QUESTIONS:​10 (This code was executed in Visual Studio Code)
#Write a Python program to sort a list of elements using the selection sort algorithm.
#Note: The selection sort improves on the bubble sort by making only one exchange for every pass through the list. 
#Sample Data:  [14,46,43,27,57,41,45,21,70] 
#Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70]


x = [14,46,43,27,57,41,45,21,70]
i = 0
while i<len(x):
    smallinteger = min(x[i:])
    index_of_smallinteger = x.index(smallinteger)
    x[i],x[index_of_smallinteger] = x[index_of_smallinteger],x[i]
    i=i+1
print (x)

#End of question 8
