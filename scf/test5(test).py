import sys

sys.stdin = open('input.txt', 'r')


def dfs(_li, _i, _j, _n, _m):
    visited = [[False] * _m for _ in range(_n)]
    di = [0, 0, 1]
    dj = [1, -1, 0]

    min_side = 1001
    tmp_side = 0

    stack = [(_i, _j)]
    while stack:
        loc = stack.pop()
        pi = loc[0]
        pj = loc[1]
        
        if not visited[pi][pj]:
            visited[pi][pj] = True
            
            for k in range(3):
                ni = pi + di[k]
                nj = pj + dj[k]

                if ni == _n:  # 맨 밑에 도달했을 때
                    if tmp_side < min_side:
                        min_side = tmp_side
                        # min_side 초기화?    

                if 0 <= ni < _n and 0 <= nj < _m:  # 범위 안에 있을 때
                    if not visited[ni][nj]:
                        visited[ni][nj] = True
                        
                        if _li[ni][nj] == '.':  # 시선이 가는 곳이면
                            if k == 2:  # 아래로 이동
                                stack.append((ni, nj))
                            else:  # 좌우로 이동
                                tmp_side += 1
                                stack.append((ni, nj))
                
    return min_side


m, n = map(int, input().split())
li = [list(input().rstrip()) for _ in range(n)]

c_list = []
for k in range(m):
    if li[0][k] == 'c':
        c_list.append([0, k])

minimum = 1001
for k in c_list:
    tmp_minimum = dfs(li, k[0], k[1], n, m)
    if tmp_minimum < minimum:
        minimun = tmp_minimum

print(minimum)