# 백준 18352 S2
# 특정 거리의 도시 찾기

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

V, E, K, X = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)

def bfs(start):
    visited = [False] * (V+1)
    visited[start] = True
    root = [[start]]
    k = 0

    while root:
        li = root.pop()
        tmp_li = []
        k += 1

        while li:
            vertex = li.pop()
        
            for next_v in graph[vertex]:
                if not visited[next_v]:
                    visited[next_v] = True
                    tmp_li.append(next_v)
        
        if k == K:
            return tmp_li
            
        if tmp_li:
            root.append(tmp_li)

    return root

res = sorted(bfs(X))
if not res:
    print(-1)
else:
    for r in res:
        print(r)