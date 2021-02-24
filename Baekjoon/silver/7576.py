# 백준 7576번 S1
# 토마토
import sys
from collections import deque

input = sys.stdin.readline

# result
result = -1

# 토마토 밭 생성
m, n = map(int, input().split())
area= []
queue = deque()

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            queue.append((i, j))
    area.append(row)


dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
while queue:
    result += 1

    for _ in range(len(queue)):
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m) and area[nx][ny] == 0:
                area[nx][ny] = 1
                queue.append((nx, ny))

for a in area:
    if 0 in a:
        result = -1

print(result)






# # result
# result = -1

# # 토마토 밭 생성
# m, n = map(int, input().split())
# area = [list(map(int, input().split())) for _ in range(n)]

# # 익은 토마토 위치
# queue = [True]
# tmp = 0
# for i in range(n):
#     for j in range(m):
#         if area[i][j] == 1:
#             queue.append((i, j))
#         elif area[i][j] == 0:
#             tmp += 1

# # 안 익은 토마토 있는지 확인
# if tmp == 0:
#     result = 0
# else:  # 안 익은 토마토가 있다면
#     visited = []
#     while len(queue) > 1:
#         loc = queue.pop(0)
#         if loc == True:
#             result += 1
#             queue.append(True)
#         else:
#             if loc not in visited:
#                 visited.append(loc)

#                 x = loc[0]
#                 y = loc[1]
#                 area[x][y] = 1

#                 dx = [0, 0, 1, -1]
#                 dy = [-1, 1, 0, 0]
#                 for i in range(4):
#                     nx = x + dx[i]
#                     ny = y + dy[i]

#                     if (0 <= nx < n) and (0 <= ny < m) and area[nx][ny] == 0:
#                         queue.append((nx, ny))

# for a in area:
#     if 0 in a:
#         result = -1

# print(result)