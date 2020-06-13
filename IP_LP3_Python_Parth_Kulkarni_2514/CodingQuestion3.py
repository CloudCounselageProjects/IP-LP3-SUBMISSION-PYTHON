#You are given n-words. Some words may repeat. For each word, output its number of               occurrences. The output order should correspond with the input order of the            appearance of the word. See the sample input/output for clarification. 
from collections import Counter
counter1 = Counter(input() for _ in range(int(input())))
print(len(counter1))
print(*counter1.values())
#Sample Input 4 bcdef abcdefg bcde bcdef 
#Sample Output 3 2 1 1 