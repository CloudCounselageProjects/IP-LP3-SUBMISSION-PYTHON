

n = int(input())
if 1<n<10**5:
    word_list = []
    word_dict = dict()

    for i in range(n):
        word = input()
        if word not in word_dict:
            word_list.append(word)
            word_dict[word] = word_dict.get(word,0) + 1

    print(len(word_list))
    for word in word_list:
        print(word_dict[word], end='')