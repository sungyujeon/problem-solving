# 백준 15654번 S3
# N과 M(5)

import sys
input = sys.stdin.readline


n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

res_list = [0] * m
visited = [False] * n

def dfs(depth, _n, _m, _li):
    global res_list
    if depth == _m:
        print(*res_list)
        return

    for i in range(_n):
        if not visited[i]:
            visited[i] = True
            res_list[depth] = _li[i]
            dfs(depth+1, _n, _m, _li)
            visited[i] = False

dfs(0, n, m, li)

