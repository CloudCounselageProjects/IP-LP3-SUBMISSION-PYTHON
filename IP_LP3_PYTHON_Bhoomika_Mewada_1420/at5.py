"""
CODING QUESTIONS:5
You have given a string. You need to remove all the duplicates from the string.
The final output string should contain each character only once. The respective order of
the characters insidestring should remain the same. You can only traverse the
string at once.
"""
#string input
s=input()
str1=""
#traversing the string only once
for i in range(len(s)):
    if s[i] not in str1:
        str1+=s[i]
print(str1)
#another method
# remove duplicates and keys the order same
# g= list(dict.fromkeys(s))
# for each in g:
#     print(each,end="")