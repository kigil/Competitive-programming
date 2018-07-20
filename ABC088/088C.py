import sys

C = [list(map(int, input().split())) for _ in range(3)]

a = [0, 1, 2]
b = [0, 1, 2]

for i in range(3):
    for j in range(3):
        a_ = list(a)
        b_ = list(b)
        del a_[i]
        del b_[i]
        if C[a_[0]][b_[0]] + C[a_[1]][b_[1]] != C[a_[1]][b_[0]] + C[a_[0]][b_[1]]:
            print("No")
            sys.exit()

print("Yes")