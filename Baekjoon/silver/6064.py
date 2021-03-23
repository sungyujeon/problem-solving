# 백준 6064번 S1
# 카잉달력
# sys.stdin = open('input.txt', 'r')

import sys
from math import gcd

def match(_M, _N, _x, _y, r):
    for i in range(r):
        nx = _x + (i * _M)
        num = nx % _N

        if num == 0:
            num = _N

        if num == _y:
            return nx
    
    return -1


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    res = 0

    _lcm = (M * N) // gcd(M, N)
    rotate = _lcm // M  # 각 수가 rotate 횟수만큼 반복
    
    if x == M and y == N:
        res = _lcm
    else:
        res = match(M, N, x, y, rotate)
    
    print(res)


# T = int(input())
# for _ in range(T):
#     M, N, x, y = map(int, input().split())
#     res = 0

#     _lcm = (M * N) // gcd(M, N)
#     rotate = _lcm // M  # 각 수가 rotate 횟수만큼 반복
    
#     if x == M and y == N:
#         res = _lcm
#     else:
#         x_available = []
#         for i in range(rotate):

#             num = x + (i*M) % N
#             while num // N:
#                 num %= N

#             x_available.append(num)
        
#         if y not in x_available:
#             res = -1
#         else:
#             y_idx = x_available.index(y)
#             res = x + (y_idx * M)
    
#     print(res)
            
    
    
    # res = kaing(M, N, x, y)
    # print(res)


# def kaing(_m, _n, flag_x, flag_y):
#     if flag_x == _m and flag_y == _n:
#         return gcd(_m, _n)

#     cnt = 0
#     _x = 0
#     _y = 0

#     while _x != _m or _y != _n:
#         if not _x % _m or _x == 0:    
#             _x = 1
#         else:
#             _x += 1
        
#         if not _y % _n or _y == 0:
#             _y = 1
#         else:
#             _y += 1

#         cnt += 1
        
#         if _x == flag_x and _y == flag_y:
#             return cnt
    
#     return -1