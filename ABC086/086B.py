
ab = list(input().split())

c = int(ab[0]+ab[1])
c_ = c**(1/2)
if c_.is_integer():
    print("Yes")
else:
    print("No")