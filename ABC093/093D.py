"""
Q = int(input())

ABlist = []

for _ in range(Q):
    ABlist.append(list(map(int, input().split())))

def function(a,b):
    ab = a*b
    k = 1
    k_ = 2
    people = 0
    while k <= k_:
        if ab % k == 0:
            k_ = ab//k - 1
        else:
            k_ = ab//k
        if k <= k_:
            if k != k_:
                if k != a and k != b:
                    people += 2
                else: people += 1
            if k ==k_:
                if k != a and k != b:
                    people += 1
        k += 1
    return people

for i in ABlist:
    a, b = i
    print(function(a,b))