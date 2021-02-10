# 백준 11726번 S3
# 2xn 타일링
import sys

input = sys.stdin.readline

N = int(input())
t = [0] * 1001
# def tiling(n):
#     if n in [1, 2]:
#         t[n] = n
#     if t[n] != 0:
#         return t[n]
#     else:
#         t[n] = tiling(n-1) + tiling(n-2)
#     return t[n]

t[1] = 1
t[2] = 2
for i in range(3, 1001):
    t[i] = t[i-1] + t[i-2]


print(t[N] % 10007)
