# 백준 10026번 G5
# 적록색약

import sys
from copy import deepcopy

input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

def dfs(_li, _i, _j, __n, _visited):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    stack = [(_i, _j)]
    color = _li[_i][_j]

    while stack:
        idx = stack.pop()
        x = idx[1]
        y = idx[0]

        if not _visited[y][x]:
            _visited[y][x] = True
            _li[y][x] = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < __n and 0 <= ny < __n and not _visited[ny][nx]:
                    if _li[ny][nx] == color:
                        stack.append((ny, nx))


def color_dfs(_li, _i, _j, __n, _visited):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    stack = [(_i, _j)]
    color = _li[_i][_j]

    while stack:
        idx = stack.pop()
        x = idx[1]
        y = idx[0]

        if not _visited[y][x]:
            _visited[y][x] = True
            _li[y][x] = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < __n and 0 <= ny < __n and not _visited[ny][nx]:
                    if color in ['R', 'G']:
                        if _li[ny][nx] in ['R', 'G']:
                            stack.append((ny, nx))
                    else:
                        if _li[ny][nx] == color:
                            stack.append((ny, nx))


def divide_area(li, _n):
    color_li = deepcopy(li)
    color_visited = [[False] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    
    color_cnt = 0
    cnt = 0
    for i in range(_n):
        for j in range(_n):
            if not color_visited[i][j]:
                color_dfs(color_li, i, j, _n, color_visited)
                color_cnt += 1

            if not visited[i][j]:
                dfs(li, i, j, _n, visited)
                cnt += 1

    return (cnt, color_cnt)

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]

result1, result2 = divide_area(arr, n)
print(result1, result2)