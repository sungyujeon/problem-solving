direction = {
    0: [0, 1],
    1: [0, -1],
    2: [1, 0],
    3: [-1, 0]
}


def setArray(grid):
    _n = len(grid)
    _array = [['' for _ in range(_n+2)] for _ in range(_n+2)]
    _outUsed = [['' for _ in range(_n+2)] for _ in range(_n+2)]

    for i in range(1, _n+1):
        for j in range(1, _n+1):
            _array[i][j] = grid[i-1][j-1]
            _outUsed[i][j] = [False] * 4

    return [_array, _outUsed]


def isInBound(_i, _j, _n):
    li = [0, _n-1]
    if (_i in li or _j in li):
        return False
    return True


def setNextIJ(ci, cj, k, n):
    _d = direction[k]
    ni = ci + _d[0]
    nj = cj + _d[1]

    if not isInBound(ni, nj, n):  # ni, nj가 범위 안이면
        if k == 0:
            nj = 1
        elif k == 1:
            nj = n - 2
        elif k == 2:
            ni = 1
        else:
            ni = n - 2

    return [ni, nj]


def getDir(_i, _j, array, k):
    _D = array[_i][_j]
    nextK = 0

    if _D == 'S':
        nextK = k
    elif _D == 'L':
        if k == 0:
            nextK = 3
        elif k == 1:
            nextK = 2
        elif k == 2:
            nextK = 0
        else:
            nextK = 1
    else:
        if k == 0:
            nextK = 2
        elif k == 1:
            nextK = 3
        elif k == 2:
            nextK = 1
        else:
            nextK = 0
    return nextK


def dfs(ci, cj, k, n, array, outUsed, res):
    if outUsed[ci][cj][k]:
        return res
    else:
        outUsed[ci][cj][k] = True

        _d = direction[k]
        [ni, nj] = setNextIJ(ci, cj, k, n)

        k = getDir(ni, nj, array, k)
        return dfs(ni, nj, k, n, array, outUsed, res+1)


def solution(grid):
    gn = len(grid)
    n = gn + 2
    res = []
    [array, outUsed] = setArray(grid)
    currDir = [0, 0]

    for i in range(1, gn+1):
        for j in range(1, gn+1):
            # 현재 -> 다음 out
            for k in range(4):
                r = dfs(i, j, k, n, array, outUsed, 0)
                if r != 0:
                    res.append(r)

    return res


grid = ["SL", "LR"]
# grid = ["S"]
print(solution(grid))
