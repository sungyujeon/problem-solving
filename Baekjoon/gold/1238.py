# 백준 1238번 G3
# 파티
# sys.stdin = open('input.txt', 'r')

import sys
import heapq
input = sys.stdin.readline

INF = 987654321
V, E, X = map(int, input().split())
out_graph = [[] for _ in range(V+1)]
in_graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    out_graph[u].append((w, v))
    in_graph[v].append((w, u))

def dijkstra(start, graph):
    d = [INF] * (V+1)
    q = [(0, start)]
    d[start] = 0

    while q:
        dist, curr_v = heapq.heappop(q)
        
        if d[curr_v] < dist:
            continue

        for next_dist, next_v in graph[curr_v]:
            total_dist = dist + next_dist
            if total_dist < d[next_v]:
                d[next_v] = total_dist
                heapq.heappush(q, (total_dist, next_v))
    return d

out_d = dijkstra(X, out_graph)  # 돌아가는 것
in_d = dijkstra(X, in_graph)  # 오는 것

res = [0] * (V+1)
for i in range(1, V+1):
    res[i] = out_d[i] + in_d[i]

print(max(res))


            