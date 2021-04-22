# 백준 4963번 S2
# 섬의 개수

# sys.stdin = open('input.txt', 'r')
import sys
input = sys.stdin.readline

def find_island(curr_i, curr_j, _li):
    global n, m
    
    stack = [(curr_i, curr_j)]
    _li[curr_i][curr_j] = 0

    di = [-1, -1, -1, 1, 1, 1, 0, 0]
    dj = [-1, 0, 1, -1, 0, 1, -1, 1]
    while stack:
        i, j = stack.pop()

        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < n and 0 <= nj < m:
                if _li[ni][nj] == 1:
                    _li[ni][nj] = 0
                    stack.append((ni, nj))


while True:
    m, n = map(int, input().split())

    if n == 0 and m == 0:
        break

    li = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    for ri in range(n):
        for rj in range(m):
            if li[ri][rj] == 1:
                find_island(ri, rj, li)
                res += 1
    print(res)
    