import sys
sys.stdin = open('input.txt', 'r')

res = 1001
def dfs(_li, _i, _j, _visited, _cnt_side, _n, _m, _side):
    global res
    
    if _i == _n-1: # 끝 행에 도착했는데 좌우 움직인 횟수가 더 작으면 res에 할당
        if res > _side:
            res = _side
        return True
    else: # 끝에 도착하지 않았을 때
        for k in [[1,0], [0,-1], [0,1]]:  # 아래 좌, 우
            ni = _i + k[0]
            nj = _j + k[1]

            # n * m 행렬
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

# 일단 0번 행에서 c(출발지점) 찾기
c_list = []
for k in range(m):
    if li[0][k] == 'c':
        c_list.append([0, k])


# 각 시작 시점에서 dfs 다 때려서 최단거리인거 찾기
for c in c_list:
    visited = [[False] * m for _ in range(n)]
    cnt_side = [[1001] * m for _ in range(n)]

    # for문에서 하나의 c에 대해 i, j 시작점을 dfs로 전달
    i, j = c[0], c[1]
    visited[i][j] = True
    cnt_side[i][j] = 0

    # dfs에 i,j 값 전달해서 dfs
    # 세로가 1000까지니까 좌우로 이동하게 되는 최악의 경우가 1000이라서 최솟값을 1001로 초기화
    f = dfs(li, i, j, visited, cnt_side, n, m, 0)
    # 아 여기서 f 값에 따라서 뭐 할라그랬는데 필요 없어서 그냥 넘어갔나보다
    # 그거 하다가 이거 통과못해서 더 못하겠으니 그냥 6번 넘어간듯 ㅋㅋㅋㅋ

if res == 1001:
    print('-1')
else:
    print(res)