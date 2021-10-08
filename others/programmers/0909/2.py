from copy import deepcopy

direction = {
    0: [0, 1],
    1: [0, -1],
    2: [1, 0],
    3: [-1, 0]
}


def setArray(grid):
    _ni = len(grid)
    _nj = len(grid[0])

    _array = [['' for _ in range(_nj+2)] for _ in range(_ni+2)]
    _outUsed = [['' for _ in range(_nj+2)] for _ in range(_ni+2)]

    for i in range(1, _ni+1):
        for j in range(1, _nj+1):
            _array[i][j] = grid[i-1][j-1]
            _outUsed[i][j] = [False] * 4

    return [_array, _outUsed]


def isInBound(_i, _j, ni2, nj2):
    if (1 <= _i < ni2-1 and 1 <= _j < nj2-1):
        return True
    return False


def setNextIJ(ci, cj, k, ni2, nj2):
    _d = direction[k]
    ni = ci + _d[0]
    nj = cj + _d[1]

    if not isInBound(ni, nj, ni2, nj2):  # ni, nj가 범위 안이면
        if k == 0:
            nj = 1
        elif k == 1:
            nj = nj2 - 2
        elif k == 2:
            ni = 1
        else:
            ni = ni2 - 2

        return [ni, nj]
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


def dfs(ci, cj, k, ni2, nj2, array, outUsed, tmpOutUsed, res):
    if tmpOutUsed[ci][cj][k]:
        return res
    else:
        tmpOutUsed[ci][cj][k] = True
        outUsed[ci][cj][k] = True

        [ni, nj] = setNextIJ(ci, cj, k, ni2, nj2)
        
        k = getDir(ni, nj, array, k)
        return dfs(ni, nj, k, ni2, nj2, array, outUsed, tmpOutUsed, res+1)



def solution(grid):
    gni = len(grid)
    gnj = len(grid[0])
    ni2 = gni + 2
    nj2 = gnj + 2
    res = []
    [array, outUsed] = setArray(grid)
    currDir = [0, 0]

    for i in range(1, gni+1):
        for j in range(1, gnj+1):
            # 현재 -> 다음 out
            for k in range(4):
                if not outUsed[i][j][k]:
                    tmpOutUsed = deepcopy(outUsed)
                    r = dfs(i, j, k, ni2, nj2, array, outUsed, tmpOutUsed, 0)
                    if r != 0:
                        res.append(r)

    return res


grid = ["SSL", "RRR"]
# grid = ["S"]
print(solution(grid))
