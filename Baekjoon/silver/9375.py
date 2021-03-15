# 백준 9375번 S3
# 패션왕 신해빈

import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

from itertools import combinations
from collections import Counter

T = int(input())

for _ in range(T):
    n = int(input())
    c = []
    for _ in range(n):
        a, b = input().rstrip().split()
        c.append(b)
    
    li = dict(Counter(c))
    li = li.values()
        

    res = 0
    for i in range(1, len(li)+1):
        perm = list(combinations(li, i))
        for j in perm:
            tmp = 1
            for k in j:
                tmp *= k
            res += tmp

    print(res)