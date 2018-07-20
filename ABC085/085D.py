
N, H = map(int, input().split())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

attack = 0

FWA = max(A)
FW = A.index(max(A))

flag = False
flag2 = False
while H > 0:
    t = max(B)  
    if H <= t:
        H -= t
        attack += 1
        print("a")
        continue
    if FWA >= t:
        t = H // FWA +1
        H = 0
        attack += t
        print("b")
        continue
    
    if len(B) == 1:
        if FWA <= t:
            h = H - t
            t = h // FWA +1
            H -= FWA * t
            attack += t
            print("c")
        else:
            t = H // FWA +1
            H = 0
            attack += t
            print("d")
        continue    
    if flag:
        h = H - D
        t = h // FWA +1
        H -= FWA * t
        attack += t
        print("e")
        continue
    
    if flag2:
        if FWA >= t:
            flag = True
            H -= FWA
        else:
            H -= t
            B.remove(t)
        attack += 1   
        print("f")
        continue
    
    W = B.index(t) 
    if FW != W:
        H -= t
        del B[W]
    else:
        flag2 = True
        D = B.pop(W)
        if FWA >= max(B):
            flag = True
            H -= FWA
        else:
            H -= max(B)
            B.remove(max(B))
        B.append(D)
    print("g")
    attack += 1
        
print(attack)