n = int(input())
word = []
for i in range(0,n):
    word.append(input())

Dict = {}
for key in word:
    Dict[key] = Dict.get(key,0)+1

print(len(Dict))   
for i in Dict.values():
    print(i ,end=" ")

print()
