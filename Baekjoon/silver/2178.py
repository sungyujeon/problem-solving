# 백준 2178번 S1
# 미로 탐색

import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, list(input().rstrip()))) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
q = deque()
q.append((0,0))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# while q:
#     idx = q.popleft()
#     x = idx[1]
#     y = idx[0]
    
#     visited[y][x] = True

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if 0 <= nx < m and 0 <= ny < n:
#             next_num = maze[ny][nx]
#             if not visited[ny][nx] and next_num == 1:
#                 q.append((ny, nx))
#                 maze[ny][nx] = maze[y][x] + 1
#                 visited[ny][nx] = True

# print(maze[n-1][m-1])



while q:
    idx = q.popleft()
    x = idx[1]
    y = idx[0]
    
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
            visited[ny][nx] = True
            next_num = maze[ny][nx]
            if next_num:
                q.append((ny, nx))
                
                adj_num = maze[y][x]
                if next_num == 1 or next_num > adj_num+1:
                    maze[ny][nx] = adj_num + 1

print(maze[n-1][m-1])
            
            

