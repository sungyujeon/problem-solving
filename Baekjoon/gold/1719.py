# 백준 1719번 G4
# 택배
# sys.stdin = open('input.txt', 'r')

import sys
import heapq
input = sys.stdin.readline

def dijkstra(s):
    global N, M, graphs, INF, res

    dp = [INF] * (N+1)
    dp[s] = 0
    q = [(s, 0)]

    while q:
        u, w = heapq.heappop(q)
        
        if w < dp[u]:
            continue
        
        for v, nw in graphs[u]:
            dist = w + nw
            if dist < dp[v]:
                dp[v] = dist
                heapq.heappush(q, (v, dist))
                res[v][s] = u
            
        

INF = 9876543210
N, M = map(int, input().split())
graphs = [[] for _ in range(N+1)]
res = [[INF] * (N+1) for _ in range(N+1)]
for _ in range(M):
    U, V, W = map(int, input().split())
    graphs[U].append((V, W))
    graphs[V].append((U, W))

for i in range(1, N+1):
    dijkstra(i)

for i in range(1, N+1):
    for j in range(1, N+1):
        if res[i][j] == INF:
            print('-', end=' ')
        else:
            print(res[i][j], end=' ')
    print()
