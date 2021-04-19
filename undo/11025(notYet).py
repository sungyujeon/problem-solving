# 백준 11025번 G2
# 요세푸스 문제3

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

max_n = 0
for i in range(24):
    if k ** i < n:
        max_n = i
    else:
        break

l = n - (k ** max_n)

res = 2 * l + 1

print(res)
    

# res = k ** _n + l