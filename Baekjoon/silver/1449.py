# 백준 1449번 S3
# 수리공 항승
import sys

input = sys.stdin.readline

n, l = map(int, input().split())
loc = list(map(int, input().split()))
loc.sort()

# [1, 2, 100, 101]
# l = 2
cnt = 0
start = loc[0]
for i in loc:
    if i < start:
        continue
    else:
        start = i + l
        cnt += 1

print(cnt)


# n, l = 4, 2
# loc = [1, 2, 100, 101]

loc2 = list(loc)
tmp_loc = []

tmp_loc.append(loc2.pop(0))
while loc2:
    if loc2[0] - tmp_loc[-1] < l:
        tmp_loc.append(loc2.pop(0))
    else:
        tmp_loc.append(-1)
        tmp_loc.append(loc2.pop(0))

cnt = 0
cnt_list = []
for i in tmp_loc:
    if i == -1:
        cnt_list.append(cnt)
        cnt = 0
    else:
        cnt += 1
cnt_list.append(cnt)

result = 0
for i in cnt_list:
    if i % l:
        result += (i // l) + 1
    else:
        result += i // l

print(result)
