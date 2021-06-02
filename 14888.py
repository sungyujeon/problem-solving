# 백준 14888번 S1
# 연산자 끼워넣기(삼성 SW 역량테스트 기출)
# sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))


MAX = -1000000001
MIN = 1000000001

def dfs(depth, result, add, sub, mul, div):
    global MAX, MIN, N, nums, opers

    if depth == N-1:
        if result > MAX:
            MAX = result
        if result < MIN:
            MIN = result
        return
    
    if add:
        dfs(depth+1, result + nums[depth+1], add-1, sub, mul, div)

    if sub:
        dfs(depth+1, result - nums[depth+1], add, sub-1, mul, div)

    if mul:
        dfs(depth+1, result * nums[depth+1], add, sub, mul-1, div)
    if div:
        tmp_res = result // nums[depth+1] if result > 0 else -1 * ((-1 * result) // nums[depth+1])
        dfs(depth+1, tmp_res, add, sub, mul, div-1)
    
dfs(0, nums[0], opers[0], opers[1], opers[2], opers[3])

print(MAX)
print(MIN)