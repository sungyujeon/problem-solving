# 백준 13424번 G4
# 비밀 모임

import sys
import heapq
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def dijkstra(s):
    global INF, N, graphs

    d = [INF] * (N+1)
    d[s] = 0
    heap = []
    heapq.heappush(heap, (s, 0))

    while heap:
        u, curr_w = heapq.heappop(heap)

        if d[u] < curr_w:
            continue

        for v, w in graphs[u]:
            next_w = w + curr_w

            if next_w < d[v]:
                d[v] = next_w
                heapq.heappush(heap, (v, next_w))
    
    return d


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    INF = 9876543210
    
    graphs = [[] for _ in range(N+1)]
    for _ in range(M):
        U, V, W = map(int, input().split())
        graphs[U].append((V, W))
        graphs[V].append((U, W))

    K = int(input())
    K_list = [INF] + list(map(int, input().split()))
    
    dk = [[0] * (N+1) for _ in range(K+1)]
    for i in range(1, K+1):
        dk[i] = dijkstra(K_list[i])
        
    dk_sum = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(1, K+1):
            dk_sum[i] += dk[j][i]

    res = 0
    min_sum = INF
    for i in range(1, N+1):
        if dk_sum[i] < min_sum:
            min_sum = dk_sum[i]
            res = i
    
    print(res)
    


    