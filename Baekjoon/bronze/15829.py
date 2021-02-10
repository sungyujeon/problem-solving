# 백준 15829번 B2
# Hashing

import sys

input = sys.stdin.readline
# 문자열 길이 l
l = int(input())
s = list(map(lambda x: ord(x) - 96, list(input().strip())))

sum = 0
for idx, al_num in enumerate(s):
    sum += al_num * (31 ** idx)

print(sum % 1234567891)