# 백준 1504번 G4
# 특정한 최단 경로(다익스트라)

# start, v1, v2, end
# start - v1 - v2 - end
# start - v2 - v1 - end
# v1 - v2 최단 경로는 한가지
sys.stdin = open('input.txt', 'r')

import sys
import heapq
input = sys.stdin.readline

INF = 987654321
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())


def dijkstra(start):
    d = [INF] * (V+1)
    d[start] = 0
    q = [(0, start)]

    while q:
        dist, u = heapq.heappop(q)
        
        if d[u] < dist:
            continue

        for w, v in graph[u]:
            next_dist = w + dist

            if next_dist < d[v]:
                d[v] = next_dist
                heapq.heappush(q, (next_dist, v))
    return d


# dijkstra
# v1 - v2
# start - v1, v2 - end
# start - v2, v1 - end
v1_d = dijkstra(v1)
v2_d = dijkstra(v2)
start_d = dijkstra(1)

v1_v2 = v1_d[v2]
v1_n = v1_d[V]
v2_n = v2_d[V]
start_v1 = start_d[v1]
start_v2 = start_d[v2]

res = min(start_v1 + v1_v2 + v2_n, start_v2 + v1_v2 + v1_n)
if res >= INF:
    print(-1)
else:
    print(res)
