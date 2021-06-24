# 백준 14395번 G5
# 4연산
# sys.stdin = open('input.txt', 'r')

import sys
from collections import deque
input = sys.stdin.readline


def bfs(s):
    global T
    
    num_set = set()
    q = deque([(s, '')])

    while q:
        num, r = q.popleft()

        if num == T:
            return r
        
        for op in ['*', '+', '/']:
            if op == '*':
                tmp = num ** 2
            elif op == '+':
                tmp = num * 2
            else:
                tmp = 1
                
            if 0 <= tmp <= T and tmp not in num_set:
                num_set.add(tmp)
                q.append((tmp, r + op))
    
    return -1

S, T = map(int, input().split())
if S == T:
    print(0)
else:
    res = bfs(S)
    print(res)