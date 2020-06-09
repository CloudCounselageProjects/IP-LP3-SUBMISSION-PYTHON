
test_case = int(input())
dictionary = dict()
while test_case:
    word = input()
    dictionary[word] = dictionary.get(word, 0) + 1
    test_case -= 1
print(len(dictionary))  # printing unique entries
for value in dictionary.values():  # printing count of all unique entries
    print(value, end=" ")
