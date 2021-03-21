import sys
input = sys.stdin.readline

n = int(input())
route = list(map(lambda x: len(x), input().rstrip().split('0')))

dp = [0] * 51
dp[1] = 1

for i in range(2, 51):
    dp[i] = dp[i-1] + dp[i-2]

res = 1
for r in route:
    res *= dp[r]

print(res)