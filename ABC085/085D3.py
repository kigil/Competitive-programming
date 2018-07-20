import sys
N, H = map(int, input().split())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

attack = 0

FWA = max(A)
B.append(0)
B.sort()

while True: 
    D = B.pop()
    if FWA >= D:
        break
    H -= D
    attack += 1
    if H <= 0:
        print(attack)
        sys.exit()

attack += H // FWA
if H % FWA > 0:
    attack += 1

print(attack)