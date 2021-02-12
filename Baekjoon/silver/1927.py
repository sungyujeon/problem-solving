# 백준 1927번 S1
# 최소 힙

import sys
import heapq

input = sys.stdin.readline

n = int(input())

li = []
for _ in range(n):
    li.append(int(input()))

heap = []
for i in li:
    if i:
        heapq.heappush(heap, i)
    else:
        if not heap:
            print('0')
        else:
            print(heapq.heappop(heap))
