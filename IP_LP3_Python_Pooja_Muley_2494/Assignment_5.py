'''You have given a string. You need to remove all the duplicates from the string.
The final output string should contain each character only once. The respective order of
the characters inside the string should remain the same. You can only traverse the
string at once.
'''


str = input()
list1 = list(str)
list2 = list()
for a in list1:
    if a not in list2:
        list2.append(a)
for a in list2:
    print(a, end="")