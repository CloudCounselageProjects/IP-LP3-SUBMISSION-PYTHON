
#CODING QUESTIONS:10
#Write a Python program to sort a list of elements using the selection sort algorithm.
#s for input of unsorted list
s=list(map(int,input().split()))

for i in range(len(s)):
    min1 = i
    for j in range(i,len(s)):
        if s[j]<=s[min1]:
            min1=j
    #showing all the passes of selection sort
    print("pass",i,":",s)
    s[min1],s[i]=s[i],s[min1]
#printing the sorted list
print(s)