# 백준 7569번 S1
# 토마토

# bfs
# 위, 아래, 가로, 세로를 돌면서
# 0이면 1로 바꾸고 depth 증가
# 처음 검사해서 0이 없는 경우는 0, 마지막에 검사해서 0이 있으면 -1, 아니면 depth
# sys.stdin = open('input.txt', 'r')


import sys
input = sys.stdin.readline

def bfs(_boxes, _t, _n, _m, _h):
    visited = [[[False] * _m for _ in range(_n)] for _ in range(_h)]
    depth = -1

    di = [-1, 1, 0, 0, 0, 0]
    dj = [0, 0, -1, 1, 0, 0]
    dh = [0, 0, 0, 0, -1, 1]

    stack = [_t]
    while stack:
        pop_tomatos = stack.pop()
        depth += 1
        
        tmp_stack = []
        while pop_tomatos:
            t = pop_tomatos.pop()
            
            for r in range(6):
                nh = t[0] + dh[r]
                ni = t[1] + di[r]
                nj = t[2] + dj[r]

                if 0 <= nh < _h and 0 <= ni < _n and 0 <= nj <_m:  # 상자 안의 범위일 때
                    if not visited[nh][ni][nj]:
                        visited[nh][ni][nj] = True

                        if _boxes[nh][ni][nj] == 0:
                            _boxes[nh][ni][nj] = 1
                            tmp_stack.append((nh, ni, nj))
        if tmp_stack:
            stack.append(tmp_stack)
    
    return depth


def check_tomato(_boxes, _n, _m, _h):
    for k in range(_h):
        for i in range(_n):
            for j in range(_m):
                if _boxes[k][i][j] == 0:
                    return False

    return True


def where_tomato(_boxes, _n, _m, _h):
    _stack = []
    for k in range(_h):
        for i in range(_n):
            for j in range(_m):
                if _boxes[k][i][j] == 1:
                    _stack.append((k, i, j))

    return _stack



m, n, h = map(int, input().split())

boxes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 토마토가 있는 곳 검사 / 모든 토마토가 0이 아닌지 검사
root_stack = where_tomato(boxes, n, m, h)
minimum_days = bfs(boxes, root_stack, n, m, h)

flag = check_tomato(boxes, n, m, h)
if not flag:  # 익지 않은 토마토가 남음
    print('-1')
else:
    print(minimum_days)