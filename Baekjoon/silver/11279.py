# 백준 11279번 S2
# 최대 힙

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
        heapq.heappush(heap, -i)
    else:
        if not heap:
            print('0')
        else:
            print(-heapq.heappop(heap))


# import sys

# input = sys.stdin.readline

# n = int(input())
# li = []
# for _ in range(n):
#     li.append(int(input()))

# heap = []
# for i in li:
#     if i:
#         heap.append(i)
#     else:
#         if not heap:
#             print('0')
#         else:
#             max_num = max(heap)
#             heap.remove(max_num)
#             print(max_num)


# import sys

# input = sys.stdin.readline

# n = int(input())
# li = []
# for _ in range(n):
#     li.append(int(input()))

# heap = []
# for i in li:
#     if i:
#         heap.append(i)
#         heap.sort()
#     else:
#         if not heap:
#             print('0')
#         else:
#             print(heap[-1])