# 백준 1260번 S2
# DFS와 BFS
import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())


def dfs(_v):
    stack = [_v]
    visited = []
    
    while stack:
        num = stack.pop()
        
        if num not in visited:
            visited.append(num)
            
            # dic[num]에 있는 리스트 추가
            tmp_list = dic[num]
            for i in range(len(tmp_list)-1, -1, -1):
                if tmp_list[i] not in visited:
                    stack.append(tmp_list[i])
    
    return visited
        

def bfs(_v):
    queue = deque()
    visited = []

    queue.append(_v)

    while queue:
        num = queue.popleft()

        if num not in visited:
            visited.append(num)
            queue.extend(dic[num])

    return visited


dic = {}
for i in range(1, n+1):
    dic[i] = []

for _ in range(m):
    a, b = map(int, input().split())

    dic[a].append(b)
    dic[b].append(a)

for i in range(1, n+1):
    dic[i].sort()

res_dfs = dfs(v)
res_bfs = bfs(v)

print(*res_dfs)
print(*res_bfs)