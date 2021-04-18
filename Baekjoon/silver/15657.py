# 백준 15767번 S3
# N과 M(8)
# sys.stdin = open('input3.txt', 'r')

import sys
input = sys.stdin.readline

def f(i, k, depth, _n, _r, _li):
    if k == depth:
        print(*_r)
        return
    
    for j in range(_n):
        num = _li[j]

        if i != 0 and num < _r[i-1]:
            continue
            
        _r[i] = num
        f(i+1, k+1, depth, _n, _r, _li)
    

n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

r = [0] * m
f(0, 0, m, n, r, li)
