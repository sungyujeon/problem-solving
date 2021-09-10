# 카카오 채용연계형 인턴십 2번
# 거리두기 확인하기

from pprint import pprint


def setArray(place):
    return [[place[i][j] for j in range(5)] for i in range(5)]


def dfs(i, j, depth, visited, arr, dx):
    def isInBound(_i, _j):
        return 0 <= _i < 5 and 0 <= _j < 5

    if depth == 2:
        return True

    for d in dx:
        ni = i + d[0]
        nj = j + d[1]
        if isInBound(ni, nj) and not visited[ni][nj]:
            if arr[ni][nj] == 'P':
                return False

            visited[ni][nj] = True
            if arr[ni][nj] == 'X':
                continue

            flag = dfs(ni, nj, depth+1, visited, arr, dx)
            if not flag:
                return False

    return True


def isDivided(arr):
    n = len(arr)
    visited = [[False for _ in range(5)] for _ in range(5)]
    dx = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'P':
                visited[i][j] = True
                r = dfs(i, j, 0, visited, arr, dx)
                if not r:
                    return 0

    return 1


def solution(places):
    res = []
    for place in places:
        arr = setArray(place)
        r = isDivided(arr)
        res.append(r)

    return res


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
                                                                                                         "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))
