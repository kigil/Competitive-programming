
X, Y = map(int, input().split())

t = X
count = 1
while True:
    t *= 2
    if t > Y:
        break
    count += 1
    
print(count)
