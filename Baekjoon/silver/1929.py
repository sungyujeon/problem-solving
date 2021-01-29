# 백준 1929번 S2
# 소수 구하기

import sys

m, n = map(int, sys.stdin.readline().split())

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** (1/2)) + 1):
        if not n % i:
            return False
    return True

prime_numbers = []
for num in range(m, n+1):
    if isPrime(num):
        print(num)