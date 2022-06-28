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

