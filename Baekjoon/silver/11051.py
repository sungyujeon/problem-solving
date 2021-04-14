# 백준 11051번 S1
# 이항계수2

import sys
from math import factorial

input = sys.stdin.readline

n, k = map(int, input().split())

fac = factorial(n) // (factorial(n-k) * factorial(k))
res = fac % 10007

print(res)