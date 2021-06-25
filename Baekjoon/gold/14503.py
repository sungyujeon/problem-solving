# 백준 14503번 G5
# 로봇 청소기
# sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline


def dfs(si, sj, di):
    global N, M, dir_dict, li

    stack = [(si, sj, di)]
    dx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    cnt = 0

    while stack:
        i, j, d = stack.pop()

        if 0 <= i < N and 0 <= j < M:
            if li[i][j] == 0:
                li[i][j] = 2
                cnt += 1
            
            flag = True
            for _ in range(4):
                d = (d + 1) % 4
                ni, nj = i + dx[d][0], j + dx[d][1]

                if 0 <= ni < N and 0 <= nj < M and li[ni][nj] == 0:
                    stack.append((ni, nj, d))
                    flag = False
                    break
            
            if flag:
                # 4방향을 다 돌았는데 청소하러 갈 공간이 없으면
                # 현재 방향에서 후진 가능한지 check
                if d == 0:
                    back_i, back_j = i + dx[2][0], j + dx[2][1]
                elif d == 1:
                    back_i, back_j = i + dx[3][0], j + dx[3][1]
                elif d == 2:
                    back_i, back_j = i + dx[0][0], j + dx[0][1]
                else:
                    back_i, back_j = i + dx[1][0], j + dx[1][1]
                
                if 0 <= back_i < N and 0 <= back_j < M and li[back_i][back_j] == 2:
                    stack.append((back_i, back_j, d))
    
    return cnt

            

N, M = map(int, input().split())
tmp = list(map(int, input().split()))
li = [list(map(int, input().split())) for _ in range(N)]
start_i, start_j = tmp[:2]
direction = tmp[2]

dir_dict = {
    0: 0,
    1: 3,
    2: 2,
    3: 1,
}
direction = dir_dict[direction]
res = dfs(start_i, start_j, direction)
print(res)

