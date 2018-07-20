import numpy as np

H, W, D = map(int,input().split())

A = []

for _ in range(H):
    A.append(list(map(int, input().split())))

A = np.array(A)

Q = int(input())

LR = []
for _ in range(Q):
  LR.append(list(map(int, input().split())))

B = np.zeros(H*W+1)
c = D + 1
while c <= H*W:
    loc = loc = np.where(A == c-D)
    i, j = map(int, loc)
    nloc = np.where(A == c)
    x, y = map(int, nloc)
    B[c] = B[c-D] + abs(x-i) + abs(y-j)
    c += 1

for lr in LR:
    l = lr[0]
    r = lr[1]
    if l == r:
        print(0)
    else:
        print(int(B[r]-B[l]))