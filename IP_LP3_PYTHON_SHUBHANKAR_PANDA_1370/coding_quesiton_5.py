'''
Coding Question 5
You have given a string. You need to remove all the duplicates from the string.
The final output string should contain each character only once. The respective order of
the characters inside the string should remain the same. You can only traverse the
string at once.
Input string:
ababacd
Output string:
abcd
'''

dict1 = {}
a=input()
a1=[]
a2=""
for i in range(len(a)):
    a1.append(a[i])
    
for i in range(len(a)):
    
    key = a[i]
    if not key in dict1.keys():
        dict1.update({key : 1})
        a2+=key
    else:
        dict1[key] += 1

print(a2)  
