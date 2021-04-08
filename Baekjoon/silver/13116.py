# 백준 13116번 S3
# 30번

import sys
input = sys.stdin.readline

T = int(input())

def make_parents(num):
    parents_set = set()
    parents_set.add(num)
    while num != 1:
        num //= 2
        parents_set.add(num)
    return parents_set


for _ in range(T):
    a, b = map(int, input().split())
    res = 1
    
    a_parents_set = make_parents(a)
    while b != 0:
        if b in a_parents_set:
            res = b
            break
        
        b //= 2


    print(res * 10)