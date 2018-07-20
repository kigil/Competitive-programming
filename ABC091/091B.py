
N = int(input())
S = []
for _ in range(N):
    S.append(input())

M = int(input())
T = []
for _ in range(M):
    T.append(input())
    
word = set(S+T)

value = [0]
for w in word:
    value.append(S.count(w)-T.count(w))
    
print(max(value))