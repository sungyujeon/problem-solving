# 백준 14502번 G5
# 연구소
# sys.stdin = open('input3.txt', 'r')

import sys
from copy import deepcopy
input = sys.stdin.readline

def seperate_virus_empty():
    global li, virus_list, empty_list, n, m
    for i in range(n):
        for j in range(m):
            if li[i][j] == 2:
                virus_list.append((i, j))
            elif li[i][j] == 0:
                empty_list.append((i, j))


def make_wall_list(_w_list, _li):
    tmp_li = deepcopy(_li)
    for wall in _w_list:
        _i, _j = wall
        tmp_li[_i][_j] = 1
    return tmp_li


res = 0
def spread_virus(_li, _virus_list, _safe_area):
    global n, m, res

    total = _safe_area
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    stack = list(_virus_list)

    while stack:
        i, j = stack.pop()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            
            if 0 <= ni < n and 0 <= nj < m:
                if _li[ni][nj] == 0:
                    _li[ni][nj] = 1
                    total -= 1

                    if res >= total:
                        return
                    stack.append((ni, nj))
    res = total
        

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

virus_list = []
empty_list = []

# virus,empty list
seperate_virus_empty()

empty_l = len(empty_list)
safe_area = empty_l -3

# wall 3개 조합으로 고르기
for i in range(empty_l-2):
    for j in range(i+1, empty_l-1):
        for k in range(j+1, empty_l):
            w_list = [empty_list[i], empty_list[j], empty_list[k]]
            wall_list = make_wall_list(w_list, li)
            
            # spread virus
            spread_virus(wall_list, virus_list, safe_area)

print(res)



