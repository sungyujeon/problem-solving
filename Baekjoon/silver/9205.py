# 백준 9205번 S1
# 맥주 마시면서 걸어가기


import sys
input = sys.stdin.readline

def d():
    for i in range(n + 2):
        for j in range(n + 2):
            if i == j: continue
            if abs(s[i][0] - s[j][0]) + abs(s[i][1] - s[j][1]) <= 1000:
                s_[i][j] = 1
                s_[j][i] = 1
def dfs(start):
    visit[start] = 1
    for i in range(n + 2):
        if s_[start][i] == 1 and visit[i] == 0:
            dfs(i)


t = int(input())
for i in range(t):
    n = int(input())
    s = [list(map(int, input().split())) for i in range(n + 2)]
    s_ = [[0] * (n + 2) for i in range(n + 2)]
    visit = [0 for i in range(n + 2)]
    d()
    dfs(0)

    if visit[n + 1] == 1:
        print("happy")
    else:
        print("sad")




# import sys

# input = sys.stdin.readline


# T = int(input())

# for _ in range(T):
#     n = int(input())
    
#     sx, sy = map(int, input().split())

#     conv = []
#     for _ in range(n):
#         x, y = map(int, input().split())
#         conv.append((x, y))
    
#     gx, gy = map(int, input().split())
#     conv.append((gx, gy))

#     result = 'sad'
#     # exec
#     while conv:
#         cx, cy = conv.pop(0)
        
#         # 현재 - 페스티벌 거리
#         sg_dist = ((gx-sx) ** 2 + (gy-sy) ** 2) ** (1/2)
#         if sg_dist <= 1000:
#             result = 'happy'
#             break
#         else:
#             # 편의점 들릴 수 있는지
#             # 현재 - 편의점 거리
#             curr_conv_dist = ((cx-sx) ** 2 + (cy-sy) ** 2) ** (1/2)
            
#             if curr_conv_dist <= 1000:
#                 sx = cx
#                 sy = cy
#             else:
#                 break
    
#     print(result)

