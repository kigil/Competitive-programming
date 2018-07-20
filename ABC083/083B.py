
N, A, B = map(int, input().split())

lst = []
for i in range(1,N+1):
    k = map(int, list(str(i)))
    a = sum(k)
    if a >= A and a <= B:
        lst.append(i)
print(sum(lst))