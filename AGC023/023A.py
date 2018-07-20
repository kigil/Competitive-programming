from math import factorial
from collections import Counter

N = int(input())
A = list(map(int, input().split()))

S = [0]

for i in A:
    S.append(S[-1] + i)

count = 0
count_dict = Counter(S)
for i in count_dict.values():
    if i == 1:
        continue
    count += factorial(i) // (factorial(i - 2) * factorial(2))
print(count)