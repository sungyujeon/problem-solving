# 백준 11659번 S3
# 구간 합 구하기4


# def intervalSum(_li, s, e):
#     total = 0
#     for i in range(s, e+1):
#         total += _li[i]
#     return total
# sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = li[i-1] + dp[i-1]

for _ in range(m):
    start, end = map(int, input().split())
    print(dp[end] - dp[start-1])