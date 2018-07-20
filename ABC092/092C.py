
N = int(input())
A = list(map(int,input().split()))
B = list(A)
B.insert(0,0)
B.append(0)

S = 0
Slist = []
for i in range(len(B)-1):
    distance = abs(B[i] - B[i+1])
    Slist.append(distance)
    S += distance

for j in range(len(A)):
    print(S + abs(B[j]-B[j+2]) - Slist[j] - Slist[j+1])

