# 백준 1197번 G4
# 최소 스패닝 트리
# sys.stdin = open('input.txt', 'r')
import sys
input = sys.stdin.readline

def find_set(x):
    global pa
    while x != pa[x]:
        x = pa[x]
    return x


def kruskal(_edges):
    global V, E, pa

    total_w = 0
    mst_cnt = 0
    for edge in _edges:
        _u, _v, _w = edge
        pa_u = find_set(_u)
        pa_v = find_set(_v)
        if pa_u != pa_v:
            total_w += _w
            mst_cnt += 1
            pa[pa_v] = pa_u
        
        if mst_cnt == V-1:  # V개의 정점을 연결하는 간선이 V-1개일 때 모든 정점이 연결
            return total_w



V, E = map(int, input().split())
pa = [i for i in range(V)]
edges = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u-1, v-1, w))
edges.sort(key=lambda x: x[2])

res = kruskal(edges)

print(res)