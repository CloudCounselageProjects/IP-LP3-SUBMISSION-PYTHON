'''
Coding Question 3
You are given n-words. Some words may repeat. For each word, output its number of
occurrences. The output order should correspond with the input order of the
appearance of the word. See the sample input/output for clarification.
Constraints
1<_n<_10 5
The sum of the lengths of all the words do not exceed 10 6
All the words are composed of lowercase English letters only.
Input Format
The first line contains the integer,n.
The next n lines each contain a word.
Output Format
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according
to their appearance in the input.
Sample Input
4
bcdef
abcdefg
bcde
bcdef
Sample Output
3
2 1 1
'''
from collections import OrderedDict

dict = OrderedDict()

for _ in range(int(input())):
    key = input()
    if not key in dict.keys():
        dict.update({key : 1})
    else:
        dict[key] += 1

print(len(dict.keys()))
print(*dict.values())

