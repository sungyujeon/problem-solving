# 프로그래머스 위클리 챌린지
# 전력망을 둘로 나누기

from collections import deque

def bfs(start, graph, visited):
    q = deque([start])
    visited[start] = True
    cnt = 1
    
    while q:
        v = q.popleft()
        
        for nextV in graph[v]:
            if not visited[nextV]:
                visited[nextV] = True
                q.append(nextV)
                cnt += 1
                
    return cnt


def solution(n, wires):
    answer = 100

    graph = [[] for _ in range(n)]
    for _v1, _v2 in wires:
        v1 = _v1 - 1
        v2 = _v2 - 1
        graph[v1].append(v2)
        graph[v2].append(v1)


    for _start, _nv in wires:
        start = _start - 1
        nv = _nv - 1
        
        visited = [False] * n
        visited[nv] = True
        tmp_cnt = bfs(start, graph, visited)
        
        tmp_answer = abs(n - (tmp_cnt * 2))
        if tmp_answer < answer:
            answer = tmp_answer

    return answer

n = 4
wires = [[1,2],[2,3],[3,4]]
print(solution(n, wires))