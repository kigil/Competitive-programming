
N = int(input())

red = []
blue = []
 
for _ in range(N):
    red.append(list(map(int, input().split())))

for _ in range(N):
    blue.append(list(map(int, input().split())))
    
match = []
for i in red:
    match.append([i[0]<j[0] and i[1]<j[1] for j in blue])

num = 0
while sum([sum(i) for i in match]) > 0:
    a = match.index(min(match))
    try:
        b = match[a].index(True)
    except ValueError:
        del match[a]
        continue
    del match[a]
    for i in match:
        i[b] = False
    num += 1
    
print(num)