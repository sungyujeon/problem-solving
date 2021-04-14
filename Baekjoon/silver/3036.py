# 백준 3036번 S3
# 링

import sys
from math import gcd

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

fr = li[0]
for i in range(1, n):
    next_ring = li[i]
    ab_gcd = gcd(fr, next_ring)
    
    a = fr // ab_gcd
    b = next_ring // ab_gcd
    print(f'{a}/{b}')
