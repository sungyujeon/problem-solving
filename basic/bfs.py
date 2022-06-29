# bfs
# - 탐색 시작 노드를 큐에 삽입하고 방문 처리
# - 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
# - 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

from pprint import pprint


#0 basic
from collections import deque

def bfs(start, graph, visited):
    
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    print()

N = 9
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]
visited = [False] * N
bfs(1, graph, visited)


#1 미로 탈출
# N x M 미로
# 최초 시작지점 (1,1) 괴물 있으면 1, 없으면 0, 미로는 반드시 탈출할 수 있는 형태
# 탈출하기 위한 최소 칸의 개수(칸 계산 시 시작/끝 칸 포함)

N, M = 5, 6  # 4 <= N, M <= 200
D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs2(arr):
    global N, M, D

    q = deque([(0, 0)])

    while q:
        i, j = q.popleft()
        
        for k in range(4):
            ni = i + D[k][0]
            nj = j + D[k][1]

            if not (0 <= ni < N and 0 <= nj < M): continue
            if arr[ni][nj] == 0: continue
            
            if arr[ni][nj] == 1:
                arr[ni][nj] = arr[i][j] + 1
                
                # optimization
                if ni == N-1 and nj == M-1:
                    return

                q.append((ni, nj))


def solution2(arr):
    global N, M
    arr = list(map(lambda x: list(map(int, list(x))), arr))
    
    bfs2(arr)
    pprint(arr)
    return arr[N-1][M-1]

arr = ['101010', '111111', '000001', '111111', '111111']
print(solution2(arr))