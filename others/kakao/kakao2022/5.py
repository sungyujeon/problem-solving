# 카카오 블라인드 2022 5번

def dfs(curr, sh, wo, r, tree, info, path):
    animal = info[curr]
    if animal == 0:  # 양
        path.append(curr)
        sh += 1
        if sh > r:
            r = sh
    elif animal == 1:  # 늑대
        wo += 1
    else:  # 이미 지나온 경로
        pass

    if sh - wo <= 0:
        if sh > r:
            r = sh
        wo -= 1
        return r, wo

    childNodes = tree[curr]
    for ch in childNodes:
        r, wo = dfs(ch, sh, wo, r, tree, info, path)

    return r, wo


def solution(info, edges):
    n = len(info)
    path = []
    tree = {}
    for i in range(n):
        tree[i] = set([])

    for pa, ch in edges:
        tree[pa].add(ch)

    i = 0
    res = 0
    wolf = 0
    while True:
        i += 1
        if i == 100:
            break
        res, wolf = dfs(0, 0, wolf, res, tree, info, path)
        for p in path:
            info[p] = -1
        path = []

    print(path)
    print(res)

    return


info = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5],
         [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]
print(solution(info, edges))
