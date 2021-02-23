# 백준 2628번 종이자르기

# w, h
# 가로 배열 >> [w(10), 4, ... 0]
# 세로 배열 >> [h(8), 3, 2 ... 0]

import sys

input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())

widths = [w, 0]
heights = [h, 0]
for _ in range(n):
    a, b = map(int, input().split())
    if a == 0:
        heights.append(b)
    else:
        widths.append(b)

# 내림차순 정렬
widths = list(reversed(sorted(widths)))
heights = list(reversed(sorted(heights)))

areas = []
for i in range(len(widths)-1):
    width = widths[i] - widths[i+1]
    for j in range(len(heights)-1):
        height = heights[j] - heights[j+1]
        area = width * height

        areas.append(area)

print(max(areas))
