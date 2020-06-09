count = {}
classes = (('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1), )
for k, v in classes:
    count[k] = count.get(k, 0)+v
print(count)
