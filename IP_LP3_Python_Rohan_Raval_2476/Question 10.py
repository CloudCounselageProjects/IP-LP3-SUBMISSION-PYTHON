
a =[]
n = int(input("Enter Range of Elements to be Sorted: "))
for i in range(0,n):
    item=int(input())
    a.append(item)
print('Unsorted List:',a)
a.sort()
print('Sorted List:',a)



"""
OUTPUT:
    
Enter Range of Elements to be Sorted: 5

4

2

6

8

3
Unsorted List: [4, 2, 6, 8, 3]
Sorted List: [2, 3, 4, 6, 8]

"""