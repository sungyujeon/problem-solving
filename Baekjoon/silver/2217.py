# 백준 2217번 S4
# 로프

import sys
input = sys.stdin.readline

n = int(input())
li = [0] * n
for i in range(n):
    li[i] = int(input())
li.sort()

res = 0
for i in range(n):
    tmp = li[i] * (n-i)
    if tmp > res:
        res = tmp

print(res)
