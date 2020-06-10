str1 = input("Enter a  string: ")
not_index = str1.find("not")
poor_index = str1.find("poor")

if poor_index > not_index and not_index != -1:
    str1 = str1.replace(str1[not_index:poor_index+4], "good")

print(str1)