num_list = []

num_list = list(input().split())
print(num_list)

for i in range(0,len(num_list)-1):
    min = i
    for j in range(i+1,len(num_list)):
        if num_list[j]<num_list[min]:
            min = j

    temp = num_list[min]
    num_list[min] = num_list[i]
    num_list[i] = temp
    #print(num_list)

print(num_list)






