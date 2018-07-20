N, Y = map(int, input().split())

flag = True
for i in range(N+1):
    x = i
    N_ = N - x
    if not(flag):
        break
    for j in range(N_+1):
        y = j
        z = N_ - j
        if 10000*x + 5000*y + 1000*z == Y:
            print(x,y,z)
            flag = False
            break
if flag:
    print(-1,-1,-1)