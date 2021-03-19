# 백준 7662번 G5
# 이중 우선순위 큐

import heapq
import sys

input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

T = int(input())

for _ in range(T):
    k = int(input())

    deleted = [True] * 1000001
    minH = []
    maxH = []

    for i in range(k):
        command, value = input().split()

        if command == 'I':
            heapq.heappush(minH, (int(value), i))
            heapq.heappush(maxH, (-int(value) ,i))
            deleted[i] = False
        else:
            if value == '1':  # 최댓값 삭제
                while maxH and deleted[maxH[0][1]]:
                    heapq.heappop(maxH)
                if maxH:
                    flag = heapq.heappop(maxH)
                    deleted[flag[1]] = True
                    
            else:  # 최솟값 삭제
                while minH and deleted[minH[0][1]]:
                    heapq.heappop(minH)
                if minH:
                    flag = heapq.heappop(minH)
                    deleted[flag[1]] = True
    
    # 삭제된 값 pop
    while maxH and deleted[maxH[0][1]]:
        heapq.heappop(maxH)
    
    while minH and deleted[minH[0][1]]:
        heapq.heappop(minH)

    if maxH:  # 배열이 있으면
        res_max = heapq.heappop(maxH)[0] * -1
        res_min = heapq.heappop(minH)[0]

        print(res_max, res_min)
    else:
        print('EMPTY')

    







# def swap_heap(_heap):
#     swap_heap = list(map(lambda x: x * (-1), _heap))
#     heapq.heapify(swap_heap)
    
#     return swap_heap
    

# T = int(input())

# for _ in range(T):
#     k = int(input())
    
#     min_heap = []
#     max_heap = []
#     for _ in range(k):
#         char, n = input().split()
#         n = int(n)

#         if char == 'I':  # insert
#             heapq.heappush(min_heap, n)
#             heapq.heappush(max_heap, -n)
#         else:  # delete
#             try:
#                 if n == -1:  # min 삭제
#                     heapq.heappop(min_heap)

#                     max_heap = swap_heap(max_heap)
#                     heapq.heapify(max_heap)
#                     heapq.heappop(max_heap)
#                     max_heap = swap_heap(max_heap)
#                     heapq.heapify(max_heap)
#                 else:  # max 삭제
#                     heapq.heappop(max_heap)
                    
#                     min_heap = swap_heap(min_heap)
#                     heapq.heapify(min_heap)
#                     heapq.heappop(min_heap)
#                     min_heap = swap_heap(min_heap)
#                     heapq.heapify(min_heap)
#             except:
#                 pass
    
#     if min_heap:
#         min_num = heapq.heappop(min_heap)
#         max_num = (-1) * heapq.heappop(max_heap)
#         print(max_num, min_num)
#     else:
#         print('EMPTY')