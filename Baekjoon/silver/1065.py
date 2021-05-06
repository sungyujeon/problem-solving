# 백준 1065번 S4
# 한수

import sys
input = sys.stdin.readline
        

n = int(input())
dp = [False] * 1001
for i in range(1, 100):
    dp[i] = True

for i in range(1, 10):
    for j in range(5):
        num1 = i * 100
        if j == 0:
            num1 += (i*10) + i
            dp[num1] = True
        else:
            if i + j + j < 10:
                num1 += (i+j) * 10 + (i+j+j)
                dp[num1] = True
            
            num1 = i * 100
            if i - j - j >= 0:
                num1 += (i-j) * 10 + (i-j-j)
                dp[num1] = True

res = 0
for i in range(1, n+1):
    if dp[i]:
        res += 1
print(res)