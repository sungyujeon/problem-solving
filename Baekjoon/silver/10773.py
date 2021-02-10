# 백준 10773번 S4
# 제로
import sys

input = sys.stdin.readline
n = int(input())

li = []
for _ in range(n):
    num = int(input())
    if not num:
        li.pop()
    else:
        li.append(num)
print(sum(li))