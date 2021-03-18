# 백준 1026번 S4
# 보물

import sys

input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
B.reverse()

res = 0
for i in range(n):
    res += A[i] * B[i]

print(res)