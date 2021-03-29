# 백준 1242번 G2
# 소풍
import sys
input = sys.stdin.readline


def fail(_n, _k, _m):
    depth = 0
    pop_num = 0
    del_num = 0
    
    while True:
        pop_num += k + depth
        depth += 1

        if pop_num > n:
            pop_num %= n
        
        if pop_num == _m:
            return depth

n, k, m = map(int, input().split())

print(fail(n, k, m))