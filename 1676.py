# 백준 1676번 S3
# 팩토리얼 0의 개수

# n부터 1까지의 수를 반복하면서
# 2,5 count
# 작은 값을 리턴

import sys

input = sys.stdin.readline

n = int(input())

cnt_2 = 0
cnt_5 = 0

for num in range(n, 1, -1):
    while not num % 2:
        num //= 2
        cnt_2 += 1

    while not num % 5:
        num //= 5
        cnt_5 += 1

print(min(cnt_2, cnt_5))