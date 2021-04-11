# 백준 10830번 G4
# 파이썬
# sys.stdin = open('input.txt', 'r')
import sys
input = sys.stdin.readline

def multiplyMatrix(_matrix1, _matrix2, _n):
    res = [[0] * _n for _ in range(_n)]
    for i in range(_n):
        for j in range(_n):
            tmp_total = 0
            for k in range(_n):
                tmp_total += _matrix1[i][k] * _matrix2[k][j]
            res[i][j] = tmp_total % 1000
    return res
        
def calcMaxBi(_b):
    num = 1
    cnt = 0
    while num <= _b:
        num *= 2
        cnt += 1
    return cnt


N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

max_length = calcMaxBi(B)
dp = [0] * max_length
dp[0] = matrix

for i in range(1, max_length):
    dp[i] = multiplyMatrix(dp[i-1], dp[i-1], N)

res = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            res[i][j] = 1

for i in range(max_length):
    if B & (1 << i):
        res = multiplyMatrix(res, dp[i], N)
        
for i in res:
    print(*i)

