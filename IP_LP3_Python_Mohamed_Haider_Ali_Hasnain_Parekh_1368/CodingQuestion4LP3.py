#CODING QUESTIONS:​5 (This code was executed in Visual Studio Code)
#You have given a string. You need to remove all the duplicates from the string. 
#The final output string should contain each character only once. The respective order of the characters inside the string should remain the same. You can only traverse the string at once. 
#Input string:  ababacd
#Output string: abcd

character = "ababacd"                           #the input string is already given in question(no user input).
list = [0] * 26
print(character)
output= ""
for ch in character:
    dup = ord(ch) - ord('a')
    if list[dup] == 0:
       output=output+ch
       list[dup] = 1
 
print(output)

#End of question 4