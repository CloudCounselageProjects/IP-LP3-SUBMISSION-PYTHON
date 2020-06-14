from collections import Counter
a = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)
student= Counter(name for name, students in a)
print(student)