
A, B, K = map(int, input().split())

ablist = list(range(A,B+1))
plist = []

for i in range(K):
    plist.append(A+i)
    plist.append(B-i)
    
plist = list(set(plist) & set(ablist))

plist.sort()

for i in plist:
    print(i)
    
"""
A, B, K = map(int, input().split())
 
X = list(range(A, min(A+K, B+1)))
Y = list(range(max(A+K, B-K+1), B+1))
for v in X + Y:
    print(v)
"""