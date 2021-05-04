# 백준 3187번 S2
# 양치기 꿍
# sys.stdin = open('input.txt', 'r')
# from pprint import pprint

import sys
input = sys.stdin.readline

def dfs(ci, cj, _visited, _li):
    global n, m, res_v, res_k

    stack = [(ci, cj)]
    _visited[ci][cj] = True
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    tmp_v = 0
    tmp_k = 0

    while stack:
        i, j = stack.pop()
        val = _li[i][j]
        
        if val == 'v':
            tmp_v += 1
        elif val == 'k':
            tmp_k += 1
        
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < n and 0 <= nj < m:
                if not _visited[ni][nj] and _li[ni][nj] != '#':
                    _visited[ni][nj] = True
                    stack.append((ni, nj))
    
    if tmp_k > tmp_v:
        res_k += tmp_k
    else:
        res_v += tmp_v


n, m = map(int, input().split())
li = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

res_v = 0
res_k = 0

for _i in range(n):
    for _j in range(m):
        if not visited[_i][_j] and li[_i][_j] != '#':
            dfs(_i, _j, visited, li)

print(res_k, res_v)