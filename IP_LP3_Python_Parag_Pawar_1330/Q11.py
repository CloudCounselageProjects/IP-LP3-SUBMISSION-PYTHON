def selectionSort(numbers):
   for fillslot in range(len(numbers)-1,0,-1):
       maxpos=0
       for location in range(1,fillslot+1):
           if numbers[location]>numbers[maxpos]:
               maxpos = location

       temp = numbers[fillslot]
       numbers[fillslot] = numbers[maxpos]
       numbers[maxpos] = temp

numbers = [14,46,43,27,57,41,45,21,70]
selectionSort(numbers)
print(numbers)

