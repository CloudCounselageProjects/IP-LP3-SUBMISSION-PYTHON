'''Write a Python program to sort a list of elements using the selection sort algorithm.
Note: The selection sort improves on the bubble sort by making only one exchange for
every pass through the list.
'''




def SelectionSort(list):
   for fillslot in range(len(list)-1,0,-1):
       maxpos=0
       for loc in range(1,fillslot+1):
           if list[loc]>list[maxpos]:
               maxpos = loc

       temp = list[fillslot]
       list[fillslot] = list[maxpos]
       list[maxpos] = temp

list = [14,46,43,27,57,41,45,21,70]
SelectionSort(list)
print(list)
