s = input()
strnot = s.find("not")
strpoor = s.find("poor")
if strpoor > strnot and strnot > 0 and strpoor > 0:
    l = s.replace(s[strnot:strpoor+4], "good")
else:
    l = s
print(l)
