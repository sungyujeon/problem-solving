
# sys.stdin = open('input.txt', 'r')
import sys
input = sys.stdin.readline


def is_arranged(_li, _n, _i, _j, _cnt):
    def _is_arranged(__li, __i, __j, _k, _visited):
        for p in range(__i, __i + _k):
            for q in range(__j, __j + _k):
                if not _visited[p][q]:
                    _visited[p][q] = True

                    if __li[p][q] == 0:  # 상품을 놓을 수 없으면
                        return False
        return True

    visited = [[False] * _n for _ in range(_n)]
    k = 1
    while _i+k-1 < _n and _j+k-1 < _n:
        if _is_arranged(_li, _i, _j, k, visited):
            _cnt[k] += 1
            k += 1
        else:
            return

cnt = [0] * 51
n = int(input())
space = [list(map(int, input().rstrip())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if space[i][j]:
            is_arranged(space, n, i, j, cnt)

print(f'total: {sum(cnt)}')

for i in range(1, len(cnt)):
    res = cnt[i]
    if res > 0:
        print(f'size[{i}]: {res}')
    else:
        break
