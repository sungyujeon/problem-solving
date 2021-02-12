# 백준 1655번 G2
# 가운데를 말해요

import sys
import heapq

input = sys.stdin.readline

n = int(input())

li = []
for _ in range(n):
    li.append(int(input()))
    li.sort()
    li_len = len(li)
    li_mean_idx = 0
    if li_len % 2:
        li_mean_idx = li_len // 2
    else:
        li_mean_idx = li_len // 2 - 1
    
    print(f'#{li[li_mean_idx]}')

# heap = []
# for _ in range(n):
#     heapq.heappush(heap, int(input()))
    
#     heap_len = len(heap)

#     heap_tmp = list(heap)
#     heapq.heapify(heap_tmp)

#     heap_tmp_len = len(heap_tmp)
#     while heap_tmp_len > 2:
#         heap_tmp.pop()
#         heapq.heappop(heap)

#     if heap_tmp_len == 2:
#         heap_tmp.pop()
#         print(f'#{heapq.heappop(heap)}')
#     else:
#         print(f'#{heapq.heappop(heap)}')