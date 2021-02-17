# 백준 1931번 S2
# 회의실 배정

import sys

input = sys.stdin.readline

n = int(input())

# 회의 시간 초기화
meeting = []
for _ in range(n):
    x, y = map(int, input().split())
    tmp_tuple = (x, y)
    meeting.append(tmp_tuple)

# 회의 시간 정렬
# 빨리 끝나는 시간 순으로 정렬 >> 그 중에서 빨리 시작하는 시간 순으로 정렬

meeting.sort(key = lambda x: (x[1], x[0]))

cnt = 0
end = 0
for time in meeting:
    if time[0] >= end:
        end = time[1]
        cnt += 1

print(cnt)