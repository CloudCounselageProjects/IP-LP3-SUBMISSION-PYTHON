string = input()
if 'not' in string and 'poor' in string:
    if string.find('not') < string.find('poor'):
        string = string[0:string.find('not')] + 'good' + string[string.find('poor') + 4:]
        print(string)
    else:
        print(string)
else:
    print(string)
