# 백준 11062번 G3
# 카드 게임

# sys.stdin = open('input.txt', 'r')
import sys
sys.setrecursionlimit(10001)
input = sys.stdin.readline

def pick(turn, i, j, cards, dp):
    if i > j: return 0
    if dp[i][j]:
        return dp[i][j]
    
    if turn:
        score = max(pick(False, i+1, j, cards, dp) + cards[i], pick(False, i, j-1, cards, dp) + cards[j])
        dp[i][j] = score
        return score
    else:
        score = min(pick(True, i+1, j, cards, dp), pick(True, i, j-1, cards, dp))
        dp[i][j] = score
        return score


T = int(input())
for _ in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    dp = [[0 for _ in range(N)] for _ in range(N)]
    pick(True, 0, N-1, cards, dp)
    print(dp[0][N-1])

