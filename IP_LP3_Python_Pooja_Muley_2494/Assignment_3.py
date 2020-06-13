'''You are given n-words. Some words may repeat. For each word, output its number of
occurrences. The output order should correspond with the input order of the
appearance of the word. See the sample input/output for clarification.
'''


no = input()
wlist = list()
d = dict()
for a in range(4):
    word = input()
    wlist.append(word)
for w in wlist:
    d[w] = d.get(w,0)+1

print(len(d))
for value in d.values():
    print(value, end=" " )