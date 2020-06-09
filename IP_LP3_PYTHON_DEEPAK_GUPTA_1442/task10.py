# 10
def selection(given_list):
    for fillslot in range(len(given_list)-1, 0, -1):
        max_pos = 0
        for location in range(1, fillslot+1):
            if given_list[location] > given_list[max_pos]:
                max_pos = location
        given_list[fillslot], given_list[max_pos] = given_list[max_pos], given_list[fillslot]

# given_list = [14,46,43,27,57,41,45,21,70]
# selection(given_list)
# print(given_list)
