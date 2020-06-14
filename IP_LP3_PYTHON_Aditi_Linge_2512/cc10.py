def selection_sort(sort_list):
    for i in range(len(sort_list)):
        smallest_element = min(sort_list[i:])
        index_of_smallest = sort_list.index(smallest_element)
        sort_list[i], sort_list[index_of_smallest] = sort_list[index_of_smallest], sort_list[i]
        #print('\nPASS :', i + 1, sort_list)
    print (sort_list)
 
 
 
lst = []
size = int(input()) #size
 
for i in range(size):
    elements = int(input())  #elements
    lst.append(elements)
 
selection_sort(lst)
