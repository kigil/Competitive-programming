import sys

N = int(input()) 

def prime_judge(N):
    if N % 2 == 0 or N % 3 ==0:
        return False
    for i in range(4,N):
        if N % i == 0:
            return False
            break
    if N % 5 == 1 :
        return True
    else: False

a = []
n = 0
p = 2

while True:
    if prime_judge(p):
        if len(a) == N:
            a2 = [str(i) for i in a]
            print(" ".join(a2))
            sys.exit()
        a.append(p)
    p += 1