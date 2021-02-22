# 백준 11399번 S3
# ATM

import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

li.sort()

result = 0
for i in range(n):
    result += li[i] * (n-i)

print(result)