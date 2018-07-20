import itertools

N = int(input())

S = []
for _ in range(N):
    S.append(input())
    
M, A, R, C, H = [], [], [], [], []

march = ["M","A","R","C","H"]

for s in S:
    top = s[0]
    if top in march:
        if top == "M":
            M.append(s)
        elif top == "A":
            A.append(s)
        elif top == "R":
            R.append(s)
        elif top == "C":
            C.append(s)
        elif top == "H":
            H.append(s)

MARCH = [len(M), len(A), len(R), len(C), len(H)]

if MARCH.count(0) >= 3:
    print(0)

else:
    x = 0
    pattern = list(itertools.combinations(MARCH, 3))
    for i in pattern:
        x += i[0]*i[1]*i[2]
    print(x)
    