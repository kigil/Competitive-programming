
s = input()

K = int(input())

s2 = [i for i in s]
s3 = [i for i in s]
S = s2

S.sort()

S = S[:K]

S = list(set(S))

S.sort()

X = []
for w in S:
    for i in range(len(s3)):
        if s3[i]==w:
            k = min(len(s3)-i, K)
            for ki in range(k):
                word = s[i:i+ki+1]
                X.append(word)
                
X = list(set(X))
X.sort()

print(X[K-1])
