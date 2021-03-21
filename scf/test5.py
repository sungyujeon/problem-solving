import sys
sys.stdin = open('input.txt', 'r')

res = 1001
def dfs(_li, _i, _j, _visited, _cnt_side, _n, _m, _side):
    global res
    
    if _i == _n-1:
        if res > _side:
            res = _side
        return True
    else:
        for k in [[1,0], [0,-1], [0,1]]:
            ni = _i + k[0]
            nj = _j + k[1]

            if 0 <= ni < _n and 0 <= nj < _m and not visited[ni][nj] and _li[ni][nj] == '.':
                if k == [1, 0]:  # 아래로
                    flag = dfs(_li, ni, nj, _visited, _cnt_side, _n, _m, _side)
                else:  # 좌우
                    _side += 1
                    if _cnt_side[ni][nj] > _side:
                        _cnt_side[ni][nj] = _side
                    else:
                        return False

                    flag = dfs(_li, ni, nj, _visited, _cnt_side, _n, _m, _side)

        return False

                    


m, n = map(int, input().split())
li = [list(input().rstrip()) for _ in range(n)]

c_list = []
for k in range(m):
    if li[0][k] == 'c':
        c_list.append([0, k])



for c in c_list:
    visited = [[False] * m for _ in range(n)]
    cnt_side = [[1001] * m for _ in range(n)]

    i, j = c[0], c[1]
    visited[i][j] = True
    cnt_side[i][j] = 0

    f = dfs(li, i, j, visited, cnt_side, n, m, 0)


if res == 1001:
    print('-1')
else:
    print(res)