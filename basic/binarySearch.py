# binary search

def binary_search(arr, target, start, end):

    if start > end:
        return -1

    mid = (start + end) // 2
    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return binary_search(arr, target, mid+1, end)
    else:
        return binary_search(arr, target, start, mid-1)
    
    

arr = [0, 1, 2, 3, 4, 5, 6, 7]
print(binary_search(arr, 1, 0, len(arr)-1))


# bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 index 반환
# bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 index 반환
from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))  # 2
print(bisect_right(a, x)) # 4

# parametric search
# 최적화 문제를 결정 문제(yes or no)로 바꾸어 해결하는 기법
# e.g. 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제


#1 떡볶이 떡 만들기
def solution1(N, M, arr):
    res = 0
    target, start, end = M, 0, max(arr)
    
    while start <= end:
        mid = (start + end) // 2
        remain = getRemain(mid, arr)
        
        if remain >= target:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return res

def getRemain(h, arr):
    total = 0
    for val in arr:
        if val > h:
            total += val - h
    return total

N, M = 4, 6
arr = [19, 15, 10, 17]
print(solution1(N, M, arr))


#2 정렬된 배열에서 특정 수의 개수 구하기
# N개 원소 오름차순 정렬, x가 등장하는 횟수 계산
# 시간복잡도 O(logN)
def solution2(n, x, arr):
    left_idx = bisect_left(arr, x)
    right_idx = bisect_right(arr, x)
    
    return right_idx - left_idx

n, x = 7, 2
arr = [1, 1, 2, 2, 2, 2, 3]
print(solution2(n, x, arr))