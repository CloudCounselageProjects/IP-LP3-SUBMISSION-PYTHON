def removeDuplicate(str, n):
    index = 0
    for i in range(0, n):


        for j in range(0, i + 1):
            if (str[i] == str[j]):
                break
        if (j == i):
            str[index] = str[i]
            index += 1

    return "".join(str[:index])
str = input()
n = len(str)
print(removeDuplicate(list(str), n))