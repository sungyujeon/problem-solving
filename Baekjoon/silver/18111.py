# 백준 18111번 S3
# 마인크래프트
from collections import Counter
import math
import sys
input = sys.stdin.readline

h, w, block = map(int, input().split())

land = []
for _ in range(h):
    land.extend(list(map(int, input().split())))
land_sum = sum(land)
land_length = len(land)
land = dict(Counter(land))

result_sec = math.inf
result_h = 0
for i in range(257):
    if i * land_length <= land_sum + block:
        tmp_sec = 0
        for k, v in land.items():
            if k > i:
                tmp_sec += 2 * v * (k - i)
            elif k < i:
                tmp_sec += v * (i - k)
        
        # tmp_sec, result_sec 비교
        if tmp_sec <= result_sec:
            result_sec = tmp_sec
            result_h = i

print(result_sec, result_h)
                



# 시간 초과
# land_area = len(land)
# height_list = list(set(land))

# # (height, height_cnt)
# height_cnt_list = []
# for height in height_list:
#     height_cnt_list.append((height, land.count(height)))

# height_cnt_list_sorted = sorted(height_cnt_list, key=lambda h: h[1], reverse=True)

# result = []
# for h in height_cnt_list_sorted:
#     time = 0
#     blocks = int(block)
#     needBlock = sum(land) - h[0] * land_area
#     if needBlock < 0 and abs(needBlock) > blocks:
#         result.append((h[0], math.inf))
#         continue
#     else:
#         for height in land:
#             diff = height - h[0]
#             if diff <= 0:
#                 for _ in range(abs(diff)):
#                     time += 1
#             else:
#                 for _ in range(abs(diff)):
#                     time += 2
#         result.append((h[0], time))

# result = sorted(result, key = lambda x: x[1])
# print(result[0][1], result[0][0])