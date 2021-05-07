# 백준 7785번 S5
# 회사에 있는 사람
# sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

n = int(input())
status_set = set()
for _ in range(n):
    name, status = input().split()

    if status == 'enter':
        status_set.add(name)
    else:
        status_set.remove(name)

res = list(status_set)
res.sort(reverse=True)

for name in res:
    print(name)