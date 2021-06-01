# 백준 4948번 S2
# 베르트랑 공준
# sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

M = 123456 * 2
prime = [True] * (M+1)
prime[0] = prime[1] = False

for i in range(2, M+1):
    if prime[i]:
        j = 2
        num = i
        while num < M+1:
            num = i * j

            if num < M+1:
                prime[num] = False
                j += 1

while True:
    n = int(input())
    if n == 0:
        break
    
    res = 0
    for i in range(n+1, (2*n)+1):
        if prime[i]:
            res += 1

    print(res)
    