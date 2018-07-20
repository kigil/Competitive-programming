import sys
X = int(input())

lim = int(X**(1/2))

listx =[]

if X == 1 or X == 2 or X ==3:
    print(1)
    sys.exit()

if X >= 4 and X <= 8:
    print(4)
    sys.exit()

for i in range(lim+1):
    if i == 0 or i ==1:
        continue
    a = i
    p = 0
    while a <= X:
        a = i ** p
        p += 1
    listx.append(i**(p-2))

print(max(listx))
        

