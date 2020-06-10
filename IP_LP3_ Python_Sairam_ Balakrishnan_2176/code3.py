
n = int(input())

word_dict = dict()

for i in range(n):
    word = input()
    if word in word_dict:
        word_dict[word] = word_dict[word] + 1
    else:
        word_dict[word] = 1

print(len(word_dict))

for key in word_dict:
    print(word_dict[key], end="")

