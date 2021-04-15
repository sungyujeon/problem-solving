# 백준 2004번 S2
# 조합 0의 개수

import sys
input = sys.stdin.readline

def count_five(num):
    cnt = 0
    while num != 0:
        num //= 5
        cnt += num
    return cnt

def count_two(num):
    cnt = 0
    while num != 0:
        num //= 2
        cnt += num
    return cnt
    
n, m = map(int, input().split())
res = min((count_five(n) - count_five(n-m) - count_five(m)), (count_two(n) - count_two(n-m) - count_two(m)))
print(res)


