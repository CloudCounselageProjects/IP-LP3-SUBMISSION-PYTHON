
from collections import OrderedDict
words=OrderedDict()
for i in range(int(input())):
    eachword=input().strip()
    words[eachword]=words.get(eachword,0)+1
print(len(words))
print(*words.values())




"""
OUTPUT:
    
input:
4

bcdef

abcdefg

bcde

bcdef

output:
3
2 1 1

"""
