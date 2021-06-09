# SWEA 4317번 A형 대비
# 칩 생산
from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def isPossible(i, j):
    global li, W, H
    if 0 <= i < H-1 and 0 <= j < W-1:
        if not (li[i][j] or li[i+1][j] or li[i+1][j+1] or li[i][j+1]):  # 1이 없으면
            return True
    return False


def dfs(cnt, u, total, r, tmp_set):
    global p_list, p_set, W, H, comb_list
    
    p_len = len(p_list)
    if cnt == p_list_len:
        if total > r:
            r = total
        return r
    

    d_ij = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    for i in range(p_len):
            
        if not u[i]:
            
            if total == 0:
                tmp_set = set([i])
            elif total == 1:
                tmp_set.add(i)
                comb_list.append(set(tmp_set))
            else:
                tmp_set.add(i)
                
                if tmp_set in comb_list:
                    break
                

            u[i] = True
            curr_i, curr_j = p_list[i]
            tmp_idx_list = []
            for j in range(8):
                ni, nj = curr_i + d_ij[j][0], curr_j + d_ij[j][1]
                if 0 <= ni < H and 0 <= nj < W and (ni, nj) in p_set:  # p_set에 있으면
                    idx = p_list.index((ni, nj))
                    if not u[idx]:
                        u[idx] = True
                        tmp_idx_list.append(idx)
            
            # dfs
            r = dfs(cnt+len(tmp_idx_list)+1, u, total+1, r, tmp_set)

            for k in tmp_idx_list:
                u[k] = False
            u[i] = False
    
    return r


T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(H)]

    comb_list = []
    p_set = set()
    for i in range(H):
        for j in range(W):
            if isPossible(i, j):
                p_set.add((i, j))
    
    p_list = list(p_set)
    p_list_len = len(p_list)
    used = [False] * p_list_len
    res = dfs(0, used, 0, 0, set())
    print(res)
    