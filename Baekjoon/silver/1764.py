# 백준 1764번 S4
# 듣보잡
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

people_dict = {}
cnt = 0
people = []
for i in range(n+m):
    if i < n:
        name = input().strip()
        people_dict[name] = name
    else:
        try:
            people.append(people_dict[input().strip()])
            cnt += 1
        except:
            continue
people.sort()
print(cnt)
for p in people:
    print(p)