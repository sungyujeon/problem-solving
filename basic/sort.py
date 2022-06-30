# sorting algorithm

from collections import deque

n = 10
base_arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


# selection sort
arr = list(base_arr)
for i in range(n-1):
    for j in range(i+1, n):
        if arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]


# insertion sort
arr = list(base_arr)
for i in range(1, n):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break


# quick sort
# pivot 설정 후 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 가장 기본적인 퀵 정렬은 첫 번째 데이터를 pivot 설정
arr = list(base_arr)
def quick_sort(array, start, end):
    if start >= end:  # 원소 1개인 경우 종료
        return

    pivot = start
    left = start + 1
    right = end
    while (left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and arr[left] <= arr[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while (right > start and arr[right] >= arr[pivot]):
            right -= 1

        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:  # 엇갈리지 않았다면
            arr[left], arr[right] = arr[right], arr[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)

quick_sort(arr, 0, n-1)

# simple quick sort for python
arr = list(base_arr)
def simple_quick_sort(arr):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return simple_quick_sort(left_side) + [pivot] + simple_quick_sort(right_side)
arr = simple_quick_sort(arr)


# counting sort
r = []
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(arr) + 1)

for i in range(len(arr)):
    count[arr[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        r.append(i)



#1 두 배열의 원소 교체
# 두 배열 A, B / 원소는 모두 자연수
# K번 바꿔치기 -> A, B 원소를 바꾸는 것
# 배열 A의 모든 원소의 합이 최대가 되게할 때 최댓값
# 5 3 A B=> 26
N, K = 5, 3  # 1 <= N <= 100_000, 0 <= K <= N
A = [1, 2]
B = []

A = deque(sorted(A))
B.sort()
res = []
while K > 0:
    if not B or not A or B[-1] <= A[0]: break
    
    b = B.pop()
    a = A.popleft()
    res.append(b)
    K -= 1

if A:
    res.extend(A)

#1 second solution
for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break



