# 백준 9375번 S3
# 패션왕 신해빈

import sys
sys.stdin = open('input.txt', 'r')

from itertools import permutations

T = int(input())

# n = 3
# clothes = {
#     1: [1,2,3],
#     2: [2,3],
#     3: [1],
# }
for _ in range(T):
    n = int(input())
    clothes = {}
    for _ in range(n):
        a, b = input().rstrip().split()
        
        try:
            clothes[b].append(a)
        except:
            clothes[b] = [a]

    cnt = len(clothes)
    li = []
    for v in clothes.values():
        li.append(len(v))

    res = 0
    for i in range(1, cnt+1):
        perm = list(permutations(li, i))
        for j in perm:
            tmp = 1
            for k in j:
                tmp *= k
            res += tmp

    print(res)