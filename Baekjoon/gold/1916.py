# 백준 1916번 G5
# 최소비용 구하기
# sys.stdin = open('input.txt', 'r')

import sys
import heapq
input = sys.stdin.readline

V = int(input())
E = int(input())
INF = 987654321

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
start, end = map(int, input().split())
d = [INF] * (V+1)

def dijkstra(s):
    q = [(s, 0)]
    d[s] = 0

    while q:
        u, w = heapq.heappop(q)
        
        if d[u] < w:
            continue

        for i in graph[u]:
            dist = w + i[1]
            if dist < d[i[0]]:
                d[i[0]] = dist
                heapq.heappush(q, (i[0], dist))

dijkstra(start)
print(d[end])
        

    