# 백준 10282번 G4
# 해킹
# sys.stdin = open('input.txt', 'r')

import sys
import heapq
input = sys.stdin.readline


def dijkstra(s):
    global V, E, graph

    q = [(s, 0)]
    d = [INF] * (V+1)
    d[s] = 0

    while q:
        u, w = heapq.heappop(q)
        
        if d[u] < w:
            continue

        for v, next_w in graph[u]:
            total_w = d[u] + next_w
            
            if total_w < d[v]:
                d[v] = total_w
                heapq.heappush(q, (v, total_w))
    return d

T = int(input())
for _ in range(T):
    INF = 987654321
    V, E, start = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    
    for _ in range(E):
        _v, _u, _w = map(int, input().split())
        graph[_u].append((_v, _w))
    
    dp = dijkstra(start)
    cnt = 0
    max_res = 0
    
    for i in range(V+1):
        dist = dp[i]
        if 0 <= dist < INF:
            cnt += 1
        
        if max_res < dist < INF:
            max_res = dist
    print(cnt, max_res)

