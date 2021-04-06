# 백준 16928번 S1
# 뱀과 사다리 게임

import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def count_dice(num):
    cnt = 0

    num -= 1
    cnt += num // 6

    if num % 6:
        cnt += 1

    return cnt
    


n, m = map(int, input().split())
board = [True] * 101
dp = [987654321] * 101
# 사다리
ladder_dict = {}
for _ in range(n):
    a, b = map(int, input().split())
    ladder_dict[a] = b

# 뱀
snake_dict = {}
for _ in range(m):
    a, b = map(int, input().split())
    board[a] = False

for i in range(1, 101):
    if board[i]:
        if i > 6:
            dp[i] = min(dp[i], count_dice(i), dp[i-1]+1, dp[i-2]+1, dp[i-3]+1, dp[i-4]+1, dp[i-5]+1, dp[i-6]+1)
        elif i == 6:
            dp[i] = min(dp[i], count_dice(i), dp[i-1]+1, dp[i-2]+1, dp[i-3]+1, dp[i-4]+1, dp[i-5]+1)
        elif i == 5:
            dp[i] = min(dp[i], count_dice(i), dp[i-1]+1, dp[i-2]+1, dp[i-3]+1, dp[i-4]+1)
        elif i == 4:
            dp[i] = min(dp[i], count_dice(i), dp[i-1]+1, dp[i-2]+1, dp[i-3]+1)
        elif i == 3:
            dp[i] = min(dp[i], count_dice(i), dp[i-1]+1, dp[i-2]+1)
        else:
            dp[i] = min(dp[i], count_dice(i), dp[i-1]+1)

        ladder = ladder_dict.get(i)
        if ladder is not None:
            dp[ladder] = min(dp[ladder], dp[i])
            for j in range(1, 7):
                k = ladder + j
                if k < 101 and board[k]:
                    dp[k] = min(dp[k], dp[i]+1)
print(dp[100])