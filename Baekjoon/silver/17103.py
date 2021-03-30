# 백준 17103번 S2
# 골드바흐 파티션

# 100만까지의 배열을 만들어 소수는 1로 초기화
# 짝수 n을 1씩 감소시키며 소수이면 (n-소수1)이 소수인지 검사 >> 맞으면 cnt++

import sys
input = sys.stdin.readline

def makePrimeList():
    _prime_list = [False, False] + ([True] * 999999)
    for i in range(2, 1000001):
        if _prime_list[i]:
            for j in range(2*i, 1000001, i):
                _prime_list[j] = False
    return _prime_list

T = int(input())
prime_list = makePrimeList()

for t in range(T):
    n = int(input())

    cnt = 0
    for i in range(n-1, (n // 2) - 1, -1):
        if prime_list[i] and prime_list[n-i]:
           cnt += 1
    print(cnt) 
