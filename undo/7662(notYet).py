# 백준 7662번 G5
# 이중 우선순위 큐

import heapq
import sys

input = sys.stdin.readline

def swap_heap(_heap):
    swap_heap = list(map(lambda x: x * (-1), _heap))
    heapq.heapify(swap_heap)
    
    return swap_heap
    

T = int(input())

for _ in range(T):
    k = int(input())
    
    min_heap = []
    max_heap = []
    for _ in range(k):
        char, n = input().split()
        n = int(n)

        if char == 'I':  # insert
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
        else:  # delete
            try:
                if n == -1:  # min 삭제
                    heapq.heappop(min_heap)

                    max_heap = swap_heap(max_heap)
                    heapq.heapify(max_heap)
                    heapq.heappop(max_heap)
                    max_heap = swap_heap(max_heap)
                    heapq.heapify(max_heap)
                else:  # max 삭제
                    heapq.heappop(max_heap)
                    
                    min_heap = swap_heap(min_heap)
                    heapq.heapify(min_heap)
                    heapq.heappop(min_heap)
                    min_heap = swap_heap(min_heap)
                    heapq.heapify(min_heap)
            except:
                pass
    
    if min_heap:
        min_num = heapq.heappop(min_heap)
        max_num = (-1) * heapq.heappop(max_heap)
        print(max_num, min_num)
    else:
        print('EMPTY')