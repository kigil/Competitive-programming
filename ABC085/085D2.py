
N, H = map(int, input().split())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

attack = 0

FWA = max(A)
FW = A.index(max(A))
D = max(B)
FA = 0


while FWA < D:
    W = B.index(D)
    if FW == W:
        FA = D
        B[W] = 0
        D = max(B)
        continue
    H -= D
    attack += 1
    B[W] = 0
    D = max(B)

if FWA >= FA:
    attack += H // FWA
    if H % FWA > 0:
        attack += 1
else:
    H -= FA
    attack += H // FWA + 1
    if H % FWA > 0:
        attack += 1
    
print(attack)
 


        
    