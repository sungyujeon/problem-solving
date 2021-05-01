# 백준 17472번 G2
# 삼성 A형 기출문제 다리만들기2
# 각 섬에 번호 붙이기 & 정점 갯수 구하기
# 각 섬에 대해 다른 다리로 갈 수 있는 '최소 가중치'를 edges list에 저장
# KRUSKAL로 MST 구하기
from pprint import pprint

import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

# 각 정점에 번호 붙이기 & 정점 갯수 구하기
def makeNoToBoard(li):
    global n, m, numberOfEdges

    def spread(_i, _j, _cnt, _li, _visited):
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]
        
        for k in range(4):
            ni = _i + di[k]
            nj = _j + dj[k]
            
            if 0 <= ni < n and 0 <= nj < m:
                if not visited[ni][nj] and _li[ni][nj]:
                    visited[ni][nj] = True
                    _li[ni][nj] = _cnt
                    spread(ni, nj, _cnt, _li, _visited)

    visited = [[False] * m for _ in range(n)]
    cnt = 1
    for i in range(n):
        for j in range(m):
            if li[i][j] and not visited[i][j]:
                visited[i][j] = True
                li[i][j] = cnt
                spread(i, j, cnt, li, visited)
                cnt += 1
    numberOfEdges = cnt - 1


def uvw(li):
    global n, m, numberOfEdges
    def find_another_island(_i, _j, _li, __adj):
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]
        u = _li[_i][_j]

        for k in range(4):
            ni = _i + di[k]
            nj = _j + dj[k]
            cnt = 0
            while 0 <= ni < n and 0 <= nj < m and _li[ni][nj] != u:
                cnt += 1

                if _li[ni][nj] != 0 and _li[ni][nj] > 0:
                    cnt -= 1
                    break
                ni += di[k]
                nj += dj[k]
            
            if cnt > 1 and 0 <= ni < n and 0 <= nj < m:
                v = _li[ni][nj]
                if cnt < __adj[u][v] or __adj[u][v] == 0:
                    __adj[u][v] = cnt
                    __adj[v][u] = cnt
    
    _adj = [[0] * (numberOfEdges+1) for _ in range(numberOfEdges+1)]
    for i in range(n):
        for j in range(m):
            if li[i][j]:  # 섬이면
                find_another_island(i, j, li, _adj)
    return _adj

    
def Kruskal(edges):
    global numberOfEdges

    def find_set(x, _pa):
        while x != _pa[x]:
            x = _pa[x]
        return x

    pa = [i for i in range(numberOfEdges)]
    used = [0] * numberOfEdges
    total = 0
    cnt = 0
    for k in edges:
        u, v, w = k
        pa_u = find_set(u, pa)
        pa_v = find_set(v, pa)
        
        if pa_u != pa_v:
            pa[pa_v] = pa[pa_u]
            total += w
            cnt += 1
        
        if cnt == numberOfEdges-1:
            break

    if cnt != numberOfEdges-1:
        total = -1
    return total
        

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
numberOfEdges = 0  # 정점의 갯수
edges_li = []  # 간선과 가중치 저장하는 리스트

# 섬에 번호 붙이기
makeNoToBoard(board)

# 인접 행렬 만들기
adj = uvw(board)

# kruskal list 만들기
for i in range(numberOfEdges+1):
    for j in range(numberOfEdges+1):
        if i > j and adj[i][j]:
            edges_li.append((i-1, j-1, adj[i][j]))
edges_li.sort(key=lambda x: x[2])

# kruskal
res = Kruskal(edges_li)
print(res)