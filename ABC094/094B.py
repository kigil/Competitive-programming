N, M, X = map(int, input().split())
A = list(map(int, input().split()))

row = [0]*(N+1)

for i in A:
    row[i]=1
    
print(min(sum(row[:X]),sum(row[X:])))