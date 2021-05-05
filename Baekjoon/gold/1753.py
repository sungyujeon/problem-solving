# 백준 1753번 G5
# 최단 경로
# sys.stdin = open('input.txt', 'r')

import sys
import heapq
input = sys.stdin.readline


def dijkstra(s):
    global dp, INF, V, E, graph, heap
    
    dp[s] = 0
    heapq.heappush(heap, (0, s))
    
    while heap:
        curr_w, u = heapq.heappop(heap)

        if dp[u] < curr_w:
            continue

        for w, v in graph[u]:
            next_w = w + curr_w

            if next_w < dp[v]:
                dp[v] = next_w
                heapq.heappush(heap, (next_w, v))


V, E = map(int, input().split())
start = int(input())

INF = 1000000
heap = []
dp = [INF] * (V+1)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

dijkstra(start)

for i in range(1, V+1):
    res = dp[i]
    if res == INF:
        res = 'INF'
    print(res)


# 일반적인 dijkstra
# def dijkstra(s, V):
#     U = [0] * (V+1)
#     U[s] = 1
#     for v in range(V+1):
#         D[v] = adj[s][v]
    
#     for _ in range(V):
#         minV = INF
#         w = 0
#         for i in range(V+1):
#             if U[i] == 0 and minV > D[i]:
#                 minV = D[i]
#                 w = i
#         U[w] = 1

#         for v in range(V+1):
#             if 0 < adj[w][v] < INF:
#                 D[v] = min(D[v], D[w] + adj[w][v])

# V, E = map(int, input().split())
# start = int(input())

# INF = 1000000
# adj = [[INF] * (V+1) for _ in range(V+1)]
# for i in range(V+1):
#     adj[i][i] = 0

# for _ in range(E):
#     u, v, w = map(int, input().split())
#     if adj[u][v] > w:
#         adj[u][v] = w

# D = [0] * (V+1)
# dijkstra(start, V)

# for i in range(1, V+1):
#     res = D[i]
#     if res == INF:
#         res = 'INF'
#     print(res)