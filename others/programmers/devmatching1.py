# 2021 데브매칭
# 행렬 테두리 회전하기

def rotate(array, query):
    si, sj, ei, ej = map(lambda x: x-1, query)
    total = 2 * (ei + ej - si - sj + 2) - 3

    minArray = []
    i, j = si, sj
    d = [0, 1]
    k = 0
    tmp = array[i][j]
    while k != total:
        if i == si and j == ej:
            d = [1, 0]
        elif i == ei and j == ej:
            d = [0, -1]
        elif i == ei and j == sj:
            d = [-1, 0]

        minArray.append(tmp)
        tmp, array[i][j] = array[i][j], tmp
        i += d[0]
        j += d[1]
        k += 1
    return min(minArray)


def solution(rows, columns, queries):
    res = []
    array = [[0 for _ in range(columns)] for _ in range(rows)]
    k = 1
    for i in range(rows):
        for j in range(columns):
            array[i][j] = k
            k += 1

    for query in queries:
        m = rotate(array, query)
        res.append(m)

    return res


rows = 6
columns = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
solution(rows, columns, queries)
