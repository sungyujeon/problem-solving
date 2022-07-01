# minimum spanning tree
# 그래프 내의 모든 정점을 포함하는 트리 중 간선의 가중치가 동일하지 않을 때의 최소 비용을 구하는 알고리즘
# greedy 알고리즘으로 분류
# - 간선 데이터를 비용에 따라 오름차순으로 정렬
# - 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
#   - 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
#   - 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않음
# - 모든 간선에 대해 두번째 과정을 반복

import heapq
from pprint import pprint

def mst(heap, V):
    total = 0
    cnt = 0
    pa = [i for i in range(V)]
    
    while heap:
        u, v, w = heapq.heappop(heap)

        pa_u = find_set(pa, u)
        pa_v = find_set(pa, v)
        
        if pa_u != pa_v:
            total += w
            cnt += 1
            pa[pa_v] = pa_u
        
        if cnt == V-1:
            return total


def find_set(pa, x):
    while x != pa[x]:
        x = pa[x]
    return x

def solution1(V, E, in_arr):
    heap = []
    for uvw in in_arr:
        u, v, w = map(int, uvw.split())
        heapq.heappush(heap, (w, u-1, v-1))
    
    res = mst(heap, V)
    return res

V, E = 3, 3  # 정점 1 <= V <= 10000, 간선 1 <= E <= 100000
in_arr = ['1 2 1', '2 3 2', '1 3 3']  # u, v, w  => 3

print(solution1(V, E, in_arr))