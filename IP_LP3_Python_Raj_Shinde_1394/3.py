# problem number 3
import numpy as np
#function to display the number of distinct words from the input.
def unique(l1):                             
    unique_list = []
    for x in l1:
        if x not in unique_list:
            unique_list.append(x)
    cnt = len(unique_list)
    print(cnt)
    
 #function to output the number of occurrences for each distinct word according to their appearance in the input.
def comp1(l1):                             
    for i in range(n-1):
        print(l1.count(l1[i]),end =" ");

n = int(input())
if 1 <= n <= pow(10,5):                         #chech input constraints
    l1 = []
    for _ in range(n):
        s1 = str(input())
        l1.append(s1)
    unique(l1)
    comp1(l1)