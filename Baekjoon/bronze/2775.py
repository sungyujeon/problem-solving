# 백준 2775번 B2
# 부녀회장이 될테야
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    apart = []

    for i in range(k+1):
        apart_floor = []
        for j in range(1, n+1):
            if not i:
                apart_floor.append(j)
            else:
                sum = 0
                for p in range(j):
                    sum += apart[i-1][p]
                apart_floor.append(sum)
        apart.append(apart_floor)
    print(apart[k][n-1])