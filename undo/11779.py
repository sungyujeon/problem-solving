# 백준 11779번 G3
# 최소비용 구하기2

import sys
sys.stdin = open('input.txt', 'r')

def dijkstra(s, end): # 시작정점 s, 마지막 정점 V
    U = [0] * V
    U[s] = 1
    for v in range(V):
        dist_sv = adj[s][v]
        D[v] = dist_sv
        if 0 < dist_sv < INF:
            P[v] = s

    #while len(U) != V:
    for _ in range(V-1):  # V = 정점개수-1과 같으므로..남은 정점개수와 같음
        minV = INF
        w = 0
        for i in range(V):
            if U[i]==0 and minV>D[i]:
                minV = D[i]
                w = i
        U[w] = 1  # 선택된 집합에 포함

        for v in range(V):   # 정점 v가
            if 0<adj[w][v]<INF:  # w에 인접이면 , 시작정점에서 w를 거쳐 v로 가능 비용과
                dist_v = D[v]
                dist_wv = D[w]+adj[w][v]
                if dist_v > dist_wv:
                    D[v] = dist_wv
                    P[v] = w
                    
                # D[v] = min(D[v], D[w]+adj[w][v])  # 시작정점에서 v로 가는 기존 비용을 비교 후 선택

INF = 100000
V = int(input())
E = int(input())
adj = [[INF]*V for _ in range(V)]
for i in range(V):
    adj[i][i] = 0
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u-1][v-1] = w  # 방향성 그래프
start, end = map(int, input().split())
P = [-1] * V
D = [0]*V
dijkstra(start-1, end-1)

# res
end -= 1
min_cost = D[end-1]
res_cnt = 0
res_path = [end+1]

while P[end] != -1:
    res_path.append(P[end]+1)
    end = P[end]
print(min_cost)
print(len(res_path))
print(*res_path[::-1])