n = int(input())
m = int(input())
list1 = []
for i in range(n):
    lst = list(input().split())
    list1.append((lst))
max_r = []
min_r = []
max_c = []
min_c = []
list2 = []
j = 0
for i in range(n):
    temp_max = max(list1[i])
    temp_min = min(list1[i])
    max_r.append(temp_max)
    min_r.append(temp_min)
    for j in range(m):
        list2.append(list1[j][i])

    temp_max = max(list2)
    temp_min = min(list2)
    max_c.append(temp_max)
    min_c.append(temp_min)
    list2 = []

max_min_list = min_r+min_c+max_r+max_c

result_set = set(max_min_list)
print(len(result_set))
print(result_set)


