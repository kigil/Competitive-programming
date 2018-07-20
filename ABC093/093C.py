
T = list(map(int, input().split()))
T.sort()
T.reverse()

ope = 0

while T[1]!=T[0]:
    ope += 1
    T[1] += 1
    T[2] += 1
    
while T[2]<T[0]:
    ope += 1
    T[2] += 2

if T[0]==T[2]:
    print(ope)
    
else:print(ope+1)