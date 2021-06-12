# 백준 11729번 S2
# 하노이 탑 이동 순서

import sys
input = sys.stdin.readline

N = int(input())


# n-1개의 원판을 3으로 옮기고
# n번 원판을 1에서 3으로 옮김
# n-1개의 원판을 2에서 3으로 옮김
def f(n, a, b, c):
    global N
    
    if n == 1:
        print(a, c)
    else:
        f(n-1, a, c, b)
        print(a, c)
        f(n-1, b, a, c)


sum = 1
for i in range(N-1):
    sum = sum * 2 + 1
print(sum)
f(N, 1, 2, 3)

