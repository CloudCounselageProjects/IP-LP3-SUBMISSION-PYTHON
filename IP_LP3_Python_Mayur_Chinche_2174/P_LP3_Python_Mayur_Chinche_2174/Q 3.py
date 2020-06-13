str = input()
new_str = []
for i in range(len(str)):
    if(str[i] not in new_str):
        new_str.append(str[i])

for ch in new_str:
    print(ch,end="")


