
S = input()
w = int(input())

word = ""
for i,s in enumerate(S):
    if i%w == 0:
        word += s

print(word)
        