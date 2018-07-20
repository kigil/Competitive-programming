
N = int(input())

S = [list(input()) for _ in range(N)]

        
def check():
    for i in range(N):
        for j in range(N-i):
            if S[i][-j] != S[-j][i]:
                return False
    return True

k = S[0]
if set(k) == 1: 
    for i in S:
        if i != k:
            break
    print(N**2)

else:
    count = 0
    for _ in range(N):
        s = S.pop(0)
        S.append(s)
        a = 0
        if check():
            count += N
    print(count)