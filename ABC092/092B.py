
N = int(input())
D, X = map(int,input().split())

A = []
for _ in range(N):
    A.append(int(input()))
    
eat = 0

for i in A:
    eat += 1 + (D-1)//i

print(eat + X)