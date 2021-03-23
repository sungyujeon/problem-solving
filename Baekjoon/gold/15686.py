# 백준 15686번 G5
# 치킨 배달

# import sys
# from itertools import combinations
# sys.stdin = open('input.txt', 'r')

# input = sys.stdin.readline

# n, m = map(int, input().split())
# li = [list(map(int, input().split())) for _ in range(n)]

# houses = []
# all_chickens = []
# for i in range(n):
#     for j in range(n):
#         if li[i][j] == 1:  # 집
#             houses.append((i,j))
#         elif li[i][j] == 2:  # 치킨집
#             all_chickens.append((i, j))

# dist = 1000000
# for ch in combinations(all_chickens, m):
#     _dist = 0
#     for house in houses:
#         _dist += min([abs(house[0] - i[0]) + abs(house[1] - i[1]) for i in ch])
#         if dist <= _dist: break;
#     if _dist < dist:
#         dist = _dist
# print(dist)



import sys
from itertools import combinations

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
            
dist = 1000000    
def distance_hc(_houses, _chickens, _n):
    global dist

    _dist = 0
    for house in _houses:
        tmp_dist_list = []
        for chicken in _chickens:
            tmp_dist_list.append(abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
    
        _dist += min(tmp_dist_list)

        if dist <= _dist:
            return
    
    if _dist < dist:
        dist = _dist

houses = []
all_chickens = []
for i in range(n):
    for j in range(n):
        if li[i][j] == 1:  # 집
            houses.append((i,j))
        elif li[i][j] == 2:  # 치킨집
            all_chickens.append((i, j))


# 치킨 집 중에 m개 뽑아서 dfs
comb_chickens = list(combinations(all_chickens, m))

# 골라진 치킨 집에서 최소 거리 bfs
for tmp_chickens in comb_chickens:
    distance_hc(houses, tmp_chickens, n)

print(dist)





# 1차 이상하게 bfs로 푼거
# def arrange_hc(__li, __houses, __chickens):
#     for house in __houses:
        
#         __li[house[0]][house[1]] = 1
    
#     for chicken in __chickens:
#         __li[chicken[0]][chicken[1]] = 2


# def bfs(__li, _i, _j, _n):
#     visited = [[False] * _n for _ in range(_n)]
#     depth = 0
    
#     di = [-1, 1, 0, 0]
#     dj = [0, 0, -1, 1]

#     stack = [[(_i, _j)]]
#     while stack:
#         h = stack.pop()
#         depth += 1

#         tmp_stack = []
#         while h:
#             _hi, _hj = h.pop()
#             visited[_hi][_hj] = True
            
#             for k in range(4):
#                 ni = _hi + di[k]
#                 nj = _hj + dj[k]

#                 if 0 <= ni < _n and 0 <= nj < _n:
#                     if not visited[ni][nj]:
#                         if __li[ni][nj] == 2:
#                             return depth
                        
#                         visited[ni][nj] = True
#                         tmp_stack.append((ni, nj))

#         stack.append(tmp_stack)

            
# dist = 1000000    
# def distance_hc(_houses, _chickens, _n):
#     global dist

#     # 집, 치킨집 배정
#     _li = [[0] * _n for _ in range(_n)]
#     arrange_hc(_li, _houses, _chickens)

#     # 각 집에서의 치킨집 거리
#     _dist = 0
#     for house in _houses:
#         hi, hj = house[0], house[1]
#         _dist += bfs(_li, hi, hj, _n)

#         if _dist > dist:
#             return
    
#     if _dist < dist:
#         dist = _dist
        
        



# n, m = map(int, input().split())
# li = [list(map(int, input().split())) for _ in range(n)]

# houses = []
# all_chickens = []
# for i in range(n):
#     for j in range(n):
#         if li[i][j] == 1:  # 집
#             houses.append((i,j))
#         elif li[i][j] == 2:  # 치킨집
#             all_chickens.append((i, j))


# # 치킨 집 중에 m개 뽑아서 dfs
# comb_chickens = list(combinations(all_chickens, m))

# # 골라진 치킨 집에서 최소 거리 bfs
# for tmp_chickens in comb_chickens:
#     distance_hc(houses, tmp_chickens, n)

# print(dist)