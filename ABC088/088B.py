
N = int(input())

A = list(map(int, input().split()))

A.sort()
A.reverse()

Alice = 0
Bob = 0

for i, num in enumerate(A):
    if i%2 == 0:
        Alice += num
    else:
        Bob += num
        
print(Alice - Bob)