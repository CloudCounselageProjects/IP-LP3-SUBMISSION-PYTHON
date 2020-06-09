# fetching string from user
input_string = input().strip()
temp_string = ""
for i in input_string:
    if i not in temp_string:
        temp_string += i
print(temp_string)
