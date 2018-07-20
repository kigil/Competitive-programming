from statistics import median
N = int(input())
X = list(map(int, input().split()))

Y = X + [0]
Z = X + [10**9 + 1]

ymed = median(Y)
zmed = median(Z)

if ymed == zmed:
    for _ in range(N):
        print(ymed)
else:
    for i in X:
        if i <= ymed:
            print(zmed)
        else:
            print(ymed)
