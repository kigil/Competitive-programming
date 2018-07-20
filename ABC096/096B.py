A, B, C = map(int, input().split())
K = int(input())

print(max(A,B,C)*(2**K-1)+A+B+C)