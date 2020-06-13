str=input("Enter string: ")
newstr=""
for x in str:
    if x not in newstr:
        newstr+=x

print(newstr)

