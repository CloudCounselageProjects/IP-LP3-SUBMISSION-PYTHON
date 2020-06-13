#CODING QUESTIONS:10
#Write a Python program to sort a list of elements using the selection sort algorithm.
#Note: The selection sort improves on the bubble sort by making only one exchange for every pass through the list.
#Sample Data:
# [14,46,43,27,57,41,45,21,70]
#Expected Result:
#[14, 21, 27, 41, 43, 45, 46, 57, 70]


def selection_sort(lst):
	for i in range(len(lst)):
		min_index = i
		for j in range(i+1, len(lst)):
			if lst[j] < lst[min_index]:
				min_index = j
		lst[i], lst[min_index] = lst[min_index], lst[i]
	return lst

list1 = []
list1 = [int(item) for item in input().split()] 
print(selection_sort(list1))

#INPUT:
#14 46 43 27 57 41 45 21 70

#OUTPUT:
#[14, 21, 27, 41, 43, 45, 46, 57, 70]
