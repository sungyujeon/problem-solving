# SWEA 4335번 A형 대비
# 무인도 탈출

# dfs
#1 하나의 상자마다 x, y, z 여섯가지 경우의 수 가능
#2 다음 상자의 x, y, z 조합이 이전 상자의 (가로 x 세로)에 들어갈 수 있는지 확인
#3 모든 상자의 경우를 따졌을 경우 return

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def dfs(level, box, u, h, r):
    global N, boxes

    if level == N:
        if h > r:
            r = h
        return r
    
    d_xyz = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]
    x, y, z = box
    for i in range(3):
        for j in range(N):
            if not u[j]:
                u[j] = True
                next_box = [boxes[j][d_xyz[i][0]], boxes[j][d_xyz[i][1]], boxes[j][d_xyz[i][2]]]
                nx, ny, nz = next_box

                if (nx <= x and ny <= y) or (ny <= x and nx <= y):
                    r = dfs(level+1, next_box, u, h+nz, r)
                else:
                    r = dfs(level+1, box, u, h, r)

                u[j] = False
    return r
    


T = int(input())
for _ in range(T):
    N = int(input())
    used = [False] * N
    boxes = [[] for _ in range(N)]
    for i in range(N):
        boxes[i] = list(map(int, input().split()))
    
    res = dfs(0, [10001 for _ in range(3)], used, 0, 0)
    
    
    print(res)
        
