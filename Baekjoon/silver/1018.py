# 백준 1018번 S5
# 체스판 다시 칠하기

import sys

n, m = map(int, sys.stdin.readline().split())
input_chess = []
for _ in range(n):
    input_chess.append(list(sys.stdin.readline()))


flag1 = []
flag2 = []
l = 0
for i in range(8):
    flag_tmp1 = []
    flag_tmp2 = []
    if l % 2:
        for j in range(8):
            if j % 2:
                flag_tmp1.append('W')
                flag_tmp2.append('B')
            else:
                flag_tmp1.append('B')
                flag_tmp2.append('W')
    else:
        for j in range(8):
            if j % 2:
                flag_tmp1.append('B')
                flag_tmp2.append('W')
            else:
                flag_tmp1.append('W')
                flag_tmp2.append('B')
    l += 1
    flag1.append(flag_tmp1)
    flag2.append(flag_tmp2)

def chess_check(p, q):
    flag1_cnt = 0
    flag2_cnt = 0
    for i in range(p, p+8):
        for j in range(q, q+8):
            if input_chess[i][j] != flag1[i-p][j-q]:
                flag1_cnt += 1
            if input_chess[i][j] != flag2[i-p][j-q]:
                flag2_cnt += 1
    return min(flag1_cnt, flag2_cnt)

flag1_cnt = 0
flag2_cnt = 0
min_cnt = []
for p in range(n-7):
    for q in range(m-7):
        min_cnt.append(chess_check(p, q))

print(min(min_cnt))