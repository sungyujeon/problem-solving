# 백준 11727번 S3
# 2 x n 타일링2

import sys

input = sys.stdin.readline

n = int(input())
li = [0] * 1001
li[1] = 1
li[2] = 3

for i in range(3, 1001):
    li[i] = li[i-1] + li[i-2]*2

print(li[n] % 10007)
