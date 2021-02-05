# 백준 1654번 S3
# 랜선 자르기
import sys

input = sys.stdin.readline

k, n = map(int, input().split())

lines = []
for _ in range(k):
    lines.append(int(input()))

max_length = sum(lines) // n

def binary(start, end):
    if start > end:
        return end
    result = 0
    cnt = 0
    mid = (start + end) // 2
    for line in lines:
        cnt += line // mid

    if cnt >= n:
        return binary(mid+1, end)
    else:
        return binary(start, mid-1)
    

print(binary(1, max_length))


# max_length = sum(lines) // n
# cnt = 0
# while True:
#     for line in lines:
#         cnt += (line // max_length)
#     if cnt == n:
#         break
#     max_length -= 1
#     cnt = 0
    
# print(max_length)