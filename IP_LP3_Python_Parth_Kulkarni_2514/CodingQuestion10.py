#Write a Python program to sort a list of elements using the selection sort algorithm.  
def ssort(list1):
    for i in range(0, len(list1) - 1):
        smallest = i
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[smallest]:
                smallest = j
        list1[i], list1[smallest] = list1[smallest], list1[i]
 
 
list1 = input('Enter the list of numbers: ').split()
list1 = [int(x) for x in list1]
ssort(list1)
print('Sorted list: ', end='')
print(list1)

#Sample Data:  [14,46,43,27,57,41,45,21,70] 
#Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70] 