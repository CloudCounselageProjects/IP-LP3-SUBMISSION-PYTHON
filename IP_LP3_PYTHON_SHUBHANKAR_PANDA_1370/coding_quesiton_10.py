'''
Coding Question 10
Write a Python program to sort a list of elements using the selection sort algorithm.
Note: The selection sort improves on the bubble sort by making only one exchange for
every pass through the list.
Sample Data:
[14,46,43,27,57,41,45,21,70]
Expected Result:
[14, 21, 27, 41, 43, 45, 46, 57, 70]
'''
def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]

alist = input().split()
alist = [int(x) for x in alist]
selection_sort(alist)
print(alist)
