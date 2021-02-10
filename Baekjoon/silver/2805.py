# 백준 2805번 S3
# 나무 자르기

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
h = list(map(int, input().split()))

start, end = 1, max(h)
while start <= end:
    mid = (start + end) // 2
    
    sum = 0
    for i in h:
        if i > mid:
            sum += i - mid
    
    if sum >= l:
        start = mid + 1
    else:
        end = mid -1
print(end)


# h.sort()
# h.reverse()

# result = 0
# if h[0] - h[1] >= l:
#     result = h[0]- l

# for i in range(h[0]-1, -1, -1):
#     sum = 0
#     for j in h:
#         if j <= i:
#             break
#         sum += j - i

#     if sum >= l:
#         result = i
#         break
# print(result)