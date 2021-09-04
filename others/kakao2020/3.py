# 카카오 2020 블라인드
# 자물쇠와 열쇠

from copy import deepcopy


def rotate(key):
    n = len(key)
    newKey = deepcopy(key)
    for i in range(n):
        for j in range(n):
            newKey[i][j] = key[n-j-1][i]
    return newKey


def isLocked(newLock, kn, k):
    for i in range(kn, kn+k):
        for j in range(kn, kn+k):
            if newLock[i][j] == 0:
                return False
    return True


def onKey(newLock, key, kn, k):
    keyLen = len(key)
    lockLen = len(newLock)
    diff = lockLen - keyLen + 1

    for i in range(diff):
        for j in range(diff):
            _newLock = deepcopy(newLock)
            flag = True
            for m in range(keyLen):
                for n in range(keyLen):
                    if (key[m][n] == 1):
                        if (_newLock[i+m][j+n] == 1):
                            flag = False
                        _newLock[i+m][j+n] = 1

            if (isLocked(_newLock, kn, k) and flag):
                return True
    return False


def solution(key, lock):
    keys = []
    tmpKey = deepcopy(key)
    for i in range(4):
        _tmpKey = rotate(tmpKey)
        keys.append(_tmpKey)
        tmpKey = _tmpKey

    n = len(lock)
    kn = len(key) - 1
    nn = n + (kn * 2)
    newLock = [[0] * nn for _ in range(nn)]

    for i in range(n):
        for j in range(n):
            newLock[i+kn][j+kn] = lock[i][j]

    for key in keys:
        res = onKey(newLock, key, kn, n)
        if res:
            return True
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
