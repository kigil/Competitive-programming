
N, X = map(int, input().split())

m = [int(input()) for _ in range(N)]

X2 = X -sum(m)

rem = X2//min(m)

print(len(m)+rem)