# 백준 1240번 G4
# 노드 사이의 거리
# 흐으으으음...............

import sys
import heapq
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# def dfs(start_node, curr_node, end_node, dist, visited):
#     # memoization에 없어서 end_node까지 온 경우
#     if curr_node == end_node:
#         D[start_node][end_node] = dist
#         D[end_node][start_node] = dist
#         return

#     # start ~ ... ~ curr_node memoization
#     if start_node != curr_node and D[start_node][curr_node] == INF:
#         D[start_node][curr_node] = dist
#         D[curr_node][start_node] = dist

#     # curr_node ~ end_node memoization 존재하는 경우
#     if D[curr_node][end_node] != INF:
#         tmp_w = dist + D[curr_node][end_node]
#         D[start_node][end_node] = tmp_w
#         D[end_node][start_node] = tmp_w
#         return
    
#     for i in range(N+1):
#         wei = graphs[curr_node][i]
#         if wei != INF and not visited[i]:
#             visited[i] = True
#             dfs(start_node, i, end_node, dist+wei, visited)
#             visited[i] = False
# def dfs(start_node, curr_node, end_node, records, visited):
#     # start ~ curr-1 dp + curr weight
#     if len(records) > 2:
#         for i in range(len(records)-2):
#             tmp_node = records[i]
#             prev_node = records[-2]

#             if D[tmp_node][curr_node] == INF:
#                 tmp_w = D[tmp_node][prev_node] + graphs[prev_node][curr_node]
#                 D[tmp_node][curr_node] = tmp_w
#                 D[curr_node][tmp_node] = tmp_w

#     for i in range(N+1):
#         wei = graphs[curr_node][i]
#         if wei != INF and not visited[i]:
#             visited[i] = True
#             records.append(i)
#             dfs(start_node, i, end_node, records, visited)
#             records.pop()
#             visited[i] = False

def dijkstra(start):
    d = [INF] * (N+1)
    d[start] = 0
    used = [False] * (N+1)

    
    q = [(0, start)]
    while q:
        w, curr_v = heapq.heappop(q)

        if used[curr_v] or d[curr_v] < w:
            continue
        
        used[curr_v] = True
        
        for i in range(N+1):
            tmp_w = graphs[curr_v][i]
            if tmp_w != INF:
                next_w = w + tmp_w
                
                if next_w < d[i] and not used[i]:
                    d[i] = next_w
                    heapq.heappush(q, (next_w, i))
    return d


INF = 10000001
N, M = map(int, input().split())
# D = [[INF] * (N+1) for _ in range(N+1)]
graphs = [[INF] * (N+1) for _ in range(N+1)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    graphs[u][v] = w
    graphs[v][u] = w
    # D[u][v] = w
    # D[v][u] = w

for _ in range(M):
    start, end = map(int, input().split())
    # visited = [False] * (N+1)
    # visited[start] = True
    # dfs(start, start, end, 0, visited)
    # dfs(start, start, end, [start], visited)
    d = dijkstra(start)
    print(d[end])
    # print(D[start][end])



    