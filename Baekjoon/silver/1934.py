# 백준 1934번 S5
# 최소공배수
# 유클리드 알고리즘으로 더 빠르게 푸는 문제

import sys
from math import gcd
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())

    ab_gcd = gcd(a, b)
    ab_lcm = a * b // ab_gcd

    print(ab_lcm)