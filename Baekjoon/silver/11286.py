# 백준 11286번 S1
# 절댓값 힙

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
        heapq.heappush(heap, (abs(i), i))
    else:
        if not heap:
            print('0')
        else:
            print(heapq.heappop(heap)[1])