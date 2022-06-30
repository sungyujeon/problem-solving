# 최단 경로 문제
# 가장 짧은 경로를 찾는 알고리즘

# dijkstra
# 특정 노드에서 출발해 다른 모든 노드로 가는 최단경로
# 음의 간선이 없을 때 정상 동작
# greedy 알고리즘으로 분류 >> 매 상황에서 가장 비용이 적은 노드 선택

# Floyd=Warshall
# 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산 O(n ** 3)

#1 전보
# N개의 도시, u -> v 간선, 전보 보내는 가중치 w
# C에서 출발해 전보가 도달하는 모든 도시의 갯수 + 각 노드가 전보 받는 데 걸리는 시간

import heapq
from pprint import pprint

def calcMsgs(arr):
    cnt = -1
    total = 0
    for val in arr:
        if val != 10e9:
            cnt += 1
            total = max(total, val)
    return (cnt, total)


def dijkstra(start, d, graph):
    hq = [(start, 0)]

    while hq:
        curr_v, curr_w = heapq.heappop(hq)

        if d[curr_v] < curr_w:
            continue
        
        for next_v, next_w in graph[curr_v]:
            cost = next_w + d[curr_v]
            if cost < d[next_v]:
                d[next_v] = cost
                heapq.heappush(hq, (next_v, cost))
    

def solution1(N, M, C, infos):
    start = C-1
    INF = 10e9
    d = [INF] * N
    d[start] = 0
    graph = [[] for _ in range(N)]

    for info in infos:
        u, v, w = list(map(int, info.split()))
        graph[u-1].append((v-1, w))
    
    dijkstra(start, d, graph)

    return calcMsgs(d)



N, M, C = 3, 2, 1  # 도시 갯수 N, 통로 갯수 M, 출발 도시 C  1 <= N <= 30_000, 1 <= M <= 200_000, 1 <= C <= N
infos = ['1 2 4', '1 3 2']  # M+1 줄에 걸쳐 X,Y,Z 정보 주어짐   1 <= X, Y <= N, 1 <= Z <= 1_000 / X에서 Y로 이어지는 통로 -> 시간 Z

print(solution1(N, M, C, infos))



#2 미래 도시
# 1 ~ N 도시는 도로로 양방향 연결 가중치는 모두 1
# 방문판매원 A는 1번 회사에 위치해 있고, K회사에 방문한 뒤 X번 회사로 가야할 때 최소 시간
# 1 <= N, M <= 100

def floyd_warshall(N, graph):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

def solution2(N, X, K, nodes):
    # target = X-1
    # m_target = K-1
    # INF = 10e9
    # graph = [[] for _ in range(N)]
    # distance = [INF] * N
    # print(target, m_target)
    
    
    # for node in nodes:
    #     u, v = map(int, node.split())
    #     graph[u-1].append((v-1, 1))
    #     graph[v-1].append((u-1, 1))
    
    # d = list(distance)
    # d[0] = 0
    # dijkstra(0, d, graph)
    # start_to_mTarget = d[m_target]
    
    # d = list(distance)
    # d[m_target] = 0
    # dijkstra(m_target, d, graph)
    # mTarget_to_target = d[target]

    # dis = start_to_mTarget + mTarget_to_target

    # if dis >= 10e9:
    #     return -1
    
    # return dis

    target = X-1
    m_target = K-1
    INF = 10e9
    graph = [[INF] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                graph[i][j] == 0
    
    for node in nodes:
        u, v = map(int, node.split())
        graph[u-1][v-1] = 1
        graph[v-1][u-1] = 1
    
    floyd_warshall(N, graph)
    res = graph[0][m_target] + graph[m_target][target]
    return res
    

N, M = 5, 7  # 회사 갯수 N, 경로의 갯수 M
X, K = 4, 5
nodes = ['1 2', '1 3', '1 4', '2 4', '3 4', '3 5', '4 5']
print(solution2(N, X, K, nodes))  #=> 3
