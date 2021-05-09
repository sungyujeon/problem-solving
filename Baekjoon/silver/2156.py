# 백준 2156번 S1
# 포도주 시식

import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


def calc(_li):
    global n
    
    dp = [0] * n
    
    if n < 2:
        return max(_li)
    elif n == 2:
        return _li[0] + _li[1]
    else:   
        dp[0] = _li[0]
        dp[1] = _li[1] + _li[0]
        dp[2] = max(dp[1], _li[2] + dp[0], _li[2] + _li[1])

        if n > 3:
            for i in range(3, n):
                dp[i] = max(dp[i-1], dp[i-2] + _li[i], dp[i-3] + _li[i-1] + _li[i])
        
        return max(dp)

n = int(input())
li = [0] * n
for i in range(n):
    li[i] = int(input())

res = calc(li)
print(res)

