def selectionSort(lst):
   for i in range(len(lst)-1,0,-1):
       maxpos=0
       for position in range(1,i+1):
           if lst[position]>lst[maxpos]:
               maxpos = position

       temp = lst[i]
       lst[i] = lst[maxpos]
       lst[maxpos] = temp

lst = []   
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) 
      

selectionSort(lst)
print(lst)
