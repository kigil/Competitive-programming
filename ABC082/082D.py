
s = input()
x, y = map(int, input().split())

point = [0,0]
xd, yd = 1,0

for i in s:
    if i == "F":
        point[0] += xd
        point[1] += yd
    else:
        if xd == 0:
            yd = 0
            if x-point[0] >= 0:
                xd = 1
            else:
                xd = -1
        else:
            xd = 0
            if y-point[1] >= 0:
                yd = 1
            else:
                yd = -1            
if point == [x,y]:
    print("Yes")
else:
    print("No")
        