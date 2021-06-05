# 백준 1002번 S4
# 터렛

# 두 점 사이의 거리: r

# 두 원 일치 : 무한대(-1) >> r == 0 and r1 == r2
# 내접 또는 외접 : 1 >> r == r1 + r2 or (r1, r2 중 큰 값) == (r1, r2 중 작은 값) + r
# 만나지 않음    : 0 >> (r1, r2, r 중 큰 값) > (나머지 두 개의 값)
# 두 점에서 만남 : 2 >> 이외의 값

# sys.stdin = open('input.txt', 'r')
import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)

    r_set = sorted([r, r1, r2], reverse=True)
    rs = sorted([r1, r2], reverse=True)

    if r == 0 and r1 == r2:
        print(-1)
    elif r == r1 + r2 or rs[0] == rs[1] + r:
        print(1)
    elif r_set[0] > r_set[1] + r_set[2]:
        print(0)
    else:
        print(2)
