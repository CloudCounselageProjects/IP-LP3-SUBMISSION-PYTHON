#coding question 11
def selectionSort(nlist):
   for fillslot in range(len(nlist)-1,0,-1):
       maxp=0
       for location in range(1,fillslot+1):
           if nlist[location]>nlist[maxp]:
               maxp = location

       temp = nlist[fillslot]
       nlist[fillslot] = nlist[maxp]
       nlist[maxp] = temp

nlist = [14,46,43,27,57,41,45,21,70]
selectionSort(nlist)
print(nlist)
