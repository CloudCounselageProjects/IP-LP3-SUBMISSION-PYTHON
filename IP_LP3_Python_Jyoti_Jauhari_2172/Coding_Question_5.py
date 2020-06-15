text = input()
text = list(text)
temp = []
for i in range(len(text)):
    if text[i] not in temp:
        temp.append(text[i])

print(''.join(temp))