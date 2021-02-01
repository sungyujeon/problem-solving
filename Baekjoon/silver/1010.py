# 백준 1010번 S5
# 다리 놓기

import sys


T = int(sys.stdin.readline())

def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def comM(number, cnt):
    result = 1
    depth = 0
    for i in range(cnt):
        result *= number - depth
        depth += 1
    return result
    

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    
    result = comM(m, n) / fac(n)
    
    print(int(result))