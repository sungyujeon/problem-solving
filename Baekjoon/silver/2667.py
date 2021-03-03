# 백준 2667번 S1
# 단지번호 붙이기

import sys

input = sys.stdin.readline

def dfs(_i, _j, _li, _visited):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    _cnt = 0

    for k in range(4):
        nx = _j + dx[k]
        ny = _i + dy[k]

        if 0 <= nx < n and 0 <= ny <n:
            if not _visited[ny][nx]:
                _visited[ny][nx] = True
                if _li[ny][nx]:  # 상하좌우 집이면
                    _cnt += 1
                    _cnt += dfs(ny, nx, _li, _visited)
    
    return _cnt


def count_houses(li, _n):
    visited = [[False] * _n for _ in range(_n)]

    cnt_li = []
    for i in range(_n):
        for j in range(_n):
            cnt = 0
            if not visited[i][j]:  # 방문하지 않았으면
                visited[i][j] = True
                if li[i][j]:  # 집이면
                    cnt += 1
                    cnt += dfs(i, j, li, visited)
                    cnt_li.append(cnt)
    
    return sorted(cnt_li)

n = int(input())
houses = [list(map(int, list(input().rstrip()))) for _ in range(n)]

result_li = count_houses(houses, n)

print(len(result_li))
for i in result_li:
    print(i)

