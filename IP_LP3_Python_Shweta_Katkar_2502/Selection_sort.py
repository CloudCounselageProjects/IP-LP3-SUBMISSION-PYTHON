def selectionSort(list):
   for x in range(len(list)-1,0,-1):
       maxpos=0
       for location in range(1,x+1):
           if list[location]>list[maxpos]:
               maxpos = location

       temp = list[x]
       list[x] = list[maxpos]
       list[maxpos] = temp

list = [14,46,43,27,57,41,45,21,70]
selectionSort(list)
print(list)

