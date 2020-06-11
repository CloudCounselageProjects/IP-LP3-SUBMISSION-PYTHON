# question 5

from collections import OrderedDict

n = input('enter the string\n')
p = ''.join(OrderedDict.fromkeys(n))
print(p)