H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]
a = 1

for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            if h == 0:
                if w == 0:
                    down, right = S[h+1][w], S[h][w+1]
                    if down == "." and right == ".":
                        print("No")
                        a = 0 
                        break
                if w == W-1:
                    down, left = S[h+1][w], S[h][w-1]
                    if down == "." and left == ".":
                        print("No")
                        a = 0 
                        break
                else:
                    down, left, right = S[h+1][w], S[h][w-1], S[h][w+1]
                    if down == "." and left == "." and right == ".":
                        print("No")
                        a = 0 
                        break
            if h == H-1:
                if w == 0:
                    up, right = S[h-1][w], S[h][w+1]
                    if up == "." and right == ".":
                        print("No")
                        a = 0 
                        break
                if w == W-1:
                    up, left = S[h-1][w], S[h][w-1]
                    if up == "." and left == ".":
                        print("No")
                        a = 0 
                        break
                else:
                    up, left, right = S[h-1][w], S[h][w-1], S[h][w+1]
                    if up == "." and left == "." and right == ".":
                        print("No")
                        a = 0 
                        break
            else:
                if w == 0:
                    up, down, right = S[h-1][w], S[h+1][w], S[h][w+1]
                    if up == "." and down == "." and right == ".":
                        print("No")
                        a = 0 
                        break
                if w == W-1:
                    up, down, left = S[h-1][w], S[h+1][w], S[h][w-1]
                    if up == "." and down == "." and left == ".":
                        print("No")
                        a = 0 
                        break
                else:
                    up, down, left, right = S[h-1][w], S[h+1][w], S[h][w-1], S[h][w+1]
                    if up == "." and down == "." and left == "." and right == ".":
                        print("No")
                        a = 0 
                        break
if a == 1:
    print("Yes")