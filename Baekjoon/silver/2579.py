# 백준 2579 S3
# 계단 오르기

# DP
# dp[n] = Sn-3(dp) + Sn-2(stairs) + n(stairs)
# dp[n] = Sn-3(dp) + Sn-1(stairs) + n(stairs)
# 둘 중에 max값이 큰 값이 dp[n]의 값이 됨

import sys
input = sys.stdin.readline


n = int(input())

stairs = [0] * (n+1)
for i in range(1, n+1):
    stairs[i] = int(input())

dp = [0] * 301

if n < 3:
    if n == 1:
        print(stairs[1])
    else:
        print(stairs[1]+stairs[2])
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[2]+stairs[3], stairs[1]+stairs[3])

    for i in range(3, n+1):
        dp1 = dp[i-3] + stairs[i-1] + stairs[i]
        dp2 = dp[i-2] + stairs[i]
        dp[i] = max(dp1, dp2)

    print(dp[n])

# def exec_dp(_n, _stairs):
#     _dp1 = [0] * (_n+1)
#     _dp2 = [0] * (_n+1)

#     if _n == 1:
#         return stairs[1]
#     elif _n == 2:
#         return max(stairs[1]+stairs[2], stairs[2])
#     else:
#         _dp1[1] = stairs[1]
#         _dp2[1] = stairs[1]

#         _dp1[2] = stairs[1] + stairs[2]
#         _dp2[2] = stairs[2]

#         _dp1[3] = stairs[2] + stairs[3]
#         _dp2[3] = stairs[1] + stairs[3]
        
#         for i in range(4, _n+1):
#             dp11 = _dp1[i-3] + _stairs[i-1] + stairs[i]
#             dp12 = _dp2[i-3] + _stairs[i-1] + stairs[i]
#             _dp1[n] = max(dp11, dp12)

#             dp21 = _dp1[i-4] + _stairs[i-2] + stairs[i]
#             dp22 = _dp2[i-3] + _stairs[i-2] + stairs[i]
#             _dp2[n] = max(dp21, dp22)
        
#     return max(_dp1[n], _dp2[n])
        
# max_value = exec_dp(n, stairs)

# print(max_value)