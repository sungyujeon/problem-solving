# 백준 1012번 S2
# 유기농 배추

# 배열을 0으로 둘러싸고
# 1. [i][j] == 1: 0으로 초기화
# 2. [i][j+1] == 1 or [i+1][j] == 1: 재귀

import sys

input = sys.stdin.readline

# 연결된 배추 뽑기 함수
def cab(_i, _j):
    global area
    visited = []
    stack = [(_i, _j)]

    while stack:
        loc = stack.pop()
        x = loc[0]
        y = loc[1]
        if area[x][y]:
            if loc not in visited:
                area[x][y] = 0
                visited.append(loc)

                loc_up = (x-1, y)
                loc_down = (x+1, y)
                loc_left = (x, y-1)
                loc_right = (x, y+1)

                stack.extend([loc_up, loc_down, loc_left, loc_right])
    
    return visited

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    area = [[0] * (m+2) for _ in range(n+2)]

    # 배추 심기
    for _ in range(k):
        a, b = map(int, input().split())
        area[b+1][a+1] = 1

    # 배추밭 모두 돌면서 cab() 함수 실행하여 심어져 있으면 뽑기(1 -> 0)
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if area[i][j]:  # cabbage == 1: cab()
                cab(i, j)
                cnt += 1  # 연결되어 있는 배추 모두 뽑으면 cnt += 1

    print(cnt)