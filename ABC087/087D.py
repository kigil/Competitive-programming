n,m = map(int, input().split())

g = [[] for _ in range(n+1)]
cood= [None for _ in range(n+1)]


def dfs(start):
    if cood[start] != None:
        return True
    stack = [start]
    cood[start] = 0
    while stack:
        v = stack.pop()
        for to, dist in g[v]:
            if cood[to] == None:
                stack.append(to)
                cood[to] = cood[v] + dist
            elif cood[v] + dist != cood[to]:
                return False
    return True

for i in range(m):
    l, r, d = map(int, input().split())
    g[l].append((r, d))
    g[r].append((l, -d))

flag = True
for i in range(1,n+1):
    if not dfs(i):
        flag = False
if flag:
    print('Yes')
else:
    print('No')


"""
N, M = map(int, input().split())
LRD = [list(map(int, input().split())) for _ in range(M)]

line = ["n"]*(N+1)
line[LRD[0][0]] = 0
for info in LRD:
    L, R, D = info
    if line[L] == "n" and line[R] == "n":
        line[L] = 0
        line[R] = D
        
    elif line[L] != "n" and line[R] == "n":
        line[R] = line[L] + D
        
    elif line[L] == "n" and line[R] != "n":
        line[L] = line[R] - D
        
    elif line[L] != "n" and line[R] != "n":
        if 
"""        
