# 백준 9663번 G5
# N-Queen

import sys
input = sys.stdin.readline

def dfs(i):
    global n, res, col, slash, backslash

    if i == n:
        res += 1
        return
    
    for j in range(n):
        if not (col[j] or slash[i+j] or backslash[i-j+n-1]):
            col[j] = slash[i+j] = backslash[i-j+n-1] = True
            dfs(i+1)
            col[j] = slash[i+j] = backslash[i-j+n-1] = False

n = int(input())
col = [False] * n
slash = [False] * (2 * n - 1)
backslash = [False] * (2 * n - 1)
res = 0

dfs(0)

print(res)

