# 백준 11653번 S4
# 소인수분해

import sys
input = sys.stdin.readline


def factorization(n):
    if n == 1:
        return
    
    i = 2
    while n != 1:
        if not n % i:
            n //= i
            print(i)
        else:
            i += 1


N = int(input())
factorization(N)
