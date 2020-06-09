# string_1 = 'The lyrics is not that poor!'#assuming a string
string_1 = input()
array = []
not_position = string_1.find('not')
poor_position = string_1.find('poor')
if not_position != -1 and not_position < poor_position:
    string_1_split = string_1.split()
    for ele in string_1_split:
        if ele != "not":
            array.append(ele)
        else:
            break
    print(' '.join(array)+' good!')
else:
    print(string_1)
