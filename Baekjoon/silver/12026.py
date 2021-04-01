# 백준 12026번 S1
# BOJ 거리
import sys
input = sys.stdin.readline

n = int(input())
block = input().rstrip()
max_value = 987654321
dp = [0] + [max_value] * (n-1)

def get_prev(_c):
    if _c == 'B':
        return 'J'
    elif _c == 'O':
        return 'B'
    else:
        return 'O'


for i in range(1, n):
    c = get_prev(block[i])
    for j in range(i):
        if block[j] == c:
            dp[i] = min(dp[i], dp[j] + (i-j) ** 2)

res = dp[i] if dp[n-1] != max_value else -1
print(res)


# res_energy = 1000000
# def boj_dist(_s, _n, _flag, _start, _end, _energy):
#     global res_energy

#     check = False
#     if _end == _n:
#         if res_energy > _energy:
#             res_energy = _energy
#         return True

#     if _flag == 'B':  # next -> O
#         while _end < _n:
#             if _s[_end] == 'O':
#                 tmp_energy = (_end - _start) ** 2
#                 check = boj_dist(_s, _n, _s[_end], _end, _end+1, _energy+tmp_energy)
#             _end += 1
#     elif _flag =='O':  # next -> J
#         while _end < _n:
#             if _s[_end] == 'J':
#                 tmp_energy = (_end - _start) ** 2
#                 check = boj_dist(_s, _n, _s[_end], _end, _end+1, _energy+tmp_energy)
#             _end += 1
#     else:  # next -> B
#         while _end < _n:
#             if _s[_end] == 'B':
#                 tmp_energy = (_end - _start) ** 2
#                 check = boj_dist(_s, _n, _s[_end], _end, _end+1, _energy+tmp_energy)
#             _end += 1

#     if check:
#         return True
#     else:
#         return False
    

# n = int(input())
# block = input().rstrip()


# flag = 'B'
# start = 0
# end = 1
# energy = 0

# res_check = boj_dist(block, n, flag, start, end, energy)
# if res_check:
#     print(res_energy)
# else:
#     print(-1)

