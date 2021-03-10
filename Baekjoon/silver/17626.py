# 백준 17626번 S5
# Four Squares

import sys

input = sys.stdin.readline

n = int(input())
dp = [0, 1]

for i in range(2, n+1):
    min_tmp = 5
    j = 1
    while j**2 <= i:
        dp_num = dp[(i - (j ** 2))] + 1
        if min_tmp > dp_num:
            min_tmp = dp_num
        j += 1
    
    dp.append(min_tmp)

print(dp[n])