
N = int(input())

A = [list(map(int, input().split())) for _ in range(2)]

get = []
for i in range(N):
    get.append(sum(A[0][:i+1])+sum(A[1][i:]))

print(max(get))