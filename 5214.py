# 백준 5214번 G1
# 환승
# sys.stdin = open('input.txt', 'r')

import sys
import heapq
from collections import deque
input = sys.stdin.readline

# INF = 100001
N, K, M = map(int, input().split())
stations = [[] for _ in range(N+1)]
hyper_list = [[] for _ in range(M)]

for i in range(M):
    tmp_stns = list(map(int, input().split()))
    hyper_list[i] = tmp_stns
    for stn in tmp_stns:
        stations[stn].append(i)

def bfs():
    visited_hypers = [False] * M
    visited = [False] * (N+1)
    visited[1] = True
    li = [stations[1]]
    cnt = 0

    while li:
        hypers = li.pop()
        tmp_q = set([])
        cnt += 1

        while hypers:
            _hyper = hypers.pop()
            stns = []
            if not visited_hypers[_hyper]:
                visited_hypers[_hyper] = True    
                stns = hyper_list[_hyper]
            
            for stn in stns:
                # res
                if stn == N:
                    return cnt + 1

                if not visited[stn]:
                    visited[stn] = True
                    tmp_q.add(stn)
        
        if tmp_q:
            tmp_hypers = set([])
            for stn in tmp_q:
                tmp_hypers.update(stations[stn])
            li.append(tmp_hypers)
    
    return -1            
            
res = bfs()
print(res)

# 일반적 계산
# INF = 100001
# N, K, M = map(int, input().split())
# graphs = [set([]) for _ in range(N+1)]
# for _ in range(M):
#     s_list = list(map(int, input().split()))
    
#     for s in s_list:
#         for _s in s_list:
#             if s != _s:
#                 graphs[s].add(_s)

# def bfs():
#     visited = [False] * (N+1)
#     q = [graphs[1]]
#     cnt = 0

#     while q:
#         next_stns = q.pop()
#         cnt += 1
        
#         tmp_stns = set([])
#         for stn in next_stns:
#             if not visited[stn]:
#                 visited[stn] = True
#                 tmp_stns.update(graphs[stn])
        
#         if tmp_stns:
#             q.append(tmp_stns)
    
#     return cnt

# def dijkstra(start):
#     d = [INF] * (N+1)
#     d[start] = 0
#     q = [(0, start)]

#     while q:
#         dist, u = heapq.heappop(q)

#         if d[u] < dist:
#             continue

#         for v in graphs[u]:
#             next_dist = 1 + dist

#             if next_dist < d[v]:
#                 d[v] = next_dist
#                 heapq.heappush(q, (next_dist, v))

#     return d


# dijkstra
# res = dijkstra(1)
# print(res[N]+1)

# res = bfs()
# if res == 0:
#     print(-1)
# else:
#     print(res)
        


