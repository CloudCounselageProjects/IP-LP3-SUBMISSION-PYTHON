import numpy as np
n=int(input("Enter the number of words: "))
list=[]
for i in range(n):
    list.append(input("Enter word :"))
x = np.array(list)
unique_list=np.unique(x)
print(len(unique_list))
for x in unique_list:
    print(list.count(x), end =' ')



