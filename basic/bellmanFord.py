# Bellman Ford
# 음수 간선에 대한 최단 경로 문제
# 음수 간선의 순환 감지 O(V * E)
# - 출발 노드 설정
# - 최단 거리 테이블 초기화
# - 다음의 과정을 N-1번 반복
#   - 전체 간선 E개를 하나씩 확인
#   - 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
# - 만약 음수 간선 순환이 발생하는지 체크하고 싶다면 3번의 과정을 한 번 더 수행
# - 이 때, 최단 거리 테이블이 갱신된다면 음수 간선 순환이 존재

from pprint import pprint

E, V = 6, 8
edges = [
    (0, 1, 6),
    (0, 2, 2),
    # (1, 2, 2),
    (1, 3, 2),
    (2, 4, 1),
    (3, 5, 2),
    (4, 1, -4),
    (4, 3, 3),
    (4, 5, 4)
]
INF = 10e9
dist = [INF] * E

def bellman_ford(start):
    global E, V, INF, edges, dist

    dist[start] = 0

    for i in range(E):
        for j in range(V):
            u, v, w = edges[j]

            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

                if i == E-1:
                    return True
    return False

negative_cycle = bellman_ford(0)

if negative_cycle:
    print(-1)
else:
    pprint(dist)
