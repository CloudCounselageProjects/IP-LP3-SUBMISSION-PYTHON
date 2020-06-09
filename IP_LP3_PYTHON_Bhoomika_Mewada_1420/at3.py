"""
CODING QUESTIONS:3
You are given n-words. Some words may repeat. For each word, output its number of
occurrences. The output order should correspond with the input order of the
appearance of the word. See the sample input/output for clarification.

"""
#no of test cases
n=int(input())
l=[]
for i in range(n):
    l.append(input())
#to remove duplicate
g= list(dict.fromkeys(s))

print(len(c))
for each in c:
    print(l.count(each),end=" ")