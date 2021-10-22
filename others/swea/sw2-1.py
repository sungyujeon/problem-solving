# 삼성 소프트웨어 역량테스트 모의 A형
# 1번

from copy import deepcopy

def getIdx(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return (i, j)
    return

def isInBound(_i, _j, N):
    if 0 <= _i < N and 0 <= _j < N:
        return True
    return False

def dfs(depth, ci, cj, current_arr, base_arr, N):
    if depth == 3:
        return

    dx = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for d in dx:
        ni = ci
        nj = cj
        cnt = 0
        while cnt < 2:
            ni += d[0]
            nj += d[1]

            if isInBound(ni, nj, N):
                if cnt == 1:  # 이미 하나의 돌을 지났으면
                    newArr = deepcopy(current_arr)
                    if current_arr[ni][nj] == 1:
                        newArr[ni][nj] = 0
                        base_arr[ni][nj] = 3
                        cnt += 1
                    newArr[ci][cj] = 0
                    dfs(depth+1, ni, nj, newArr, base_arr, N)
                else:
                    if current_arr[ni][nj] == 1:
                        cnt += 1
            else:
                break

T = int(input())
for test_case in range(1, T + 1):
    res = 0
    N = int(input())

    base_arr = [list(map(int, input().split())) for _ in range(N)]
    currentArr = deepcopy(base_arr)
    ti, tj = getIdx(base_arr, N)
    dfs(0, ti, tj, currentArr, base_arr, N)

    for i in range(N):
        for j in range(N):
            if base_arr[i][j] == 3:
                res += 1

    print("#%d %d" % (test_case+1, res))