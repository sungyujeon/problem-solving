# 백준 11004번 K번째 수
# K번째 수
# merge sort 이용

# quick sort가 최악의 경우 O(n ** 2)의 시간 복잡도를 요구할 수 있는 반면
# merge sort는 항상 O(nlogn)의 시간 복잡도를 요구하므로 안정적

# quick sort: pivot을 통해 정렬 -> 영역을 쪼개 정렬(추가 학습 필요)
# merge sort: 영역을 쪼갬 -> 각 영역을 정렬
# sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

def merge(array, left, mid, right):
    left_array = array[left:mid+1]
    right_array = array[mid+1:right+1]
    
    l_length = len(left_array)
    r_length = len(right_array)
    i = j = 0
    k = left

    while i < l_length and j < r_length:
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1
    
    while i < l_length:
        array[k] = left_array[i]
        k += 1
        i += 1
    
    while j < r_length:
        array[k] = right_array[j]
        k += 1
        j += 1
    
        

def mergeSort(array, left, right):
    if left < right:
        mid = (left + right) // 2

        mergeSort(array, left, mid)
        mergeSort(array, mid+1, right)
        merge(array, left, mid, right)
    


N, K = map(int, input().split())
li = list(map(int, input().split()))
# mergeSort(li, 0, len(li) - 1)
li.sort()
print(li[K-1])



