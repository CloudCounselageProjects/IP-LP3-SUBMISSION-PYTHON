from collections import Counter
cls = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
    ('VIII', 2)
)
students = Counter(class_name for class_name, no_students in cls)
print(students)

print(type(cls))
print(type(students))