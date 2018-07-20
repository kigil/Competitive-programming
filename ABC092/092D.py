
A, B = map(int,input().split())

grid = []

for _ in range(50):
    grid.append(["#"]*100)
for _ in range(50):
    grid.append(["."]*100)
    
for i in range(A-1):
    grid[2*(i//50)][(i*2)%100] = "."

for i in range(B-1):
    grid[99 - 2*(i//50)][(i*2)%100] = "#"
    
print("100 100")
for i in grid:
    p = "".join(i)
    print(p)