N = 0
MAX_CNT = 0
def solution(arr, k):
    global N, MAX_CNT

    N = len(arr)
    MAX_CNT = (N * (N-1)) // 2
    
    m_sort(arr, 0, k)
    

    return MAX_CNT

def isSort(arr):
    global N

    for i in range(N):
        if arr[i] != i+1:
            return False
    return True

def swap(arr, idx1, idx2):
    num1, num2 = arr[idx1], arr[idx2]
    if num1 > num2:
        arr[idx1], arr[idx2] = num2, num1
        return True
    return False

def m_sort(arr, cnt, k):
    global N, MAX_CNT

    if isSort(arr):
        if cnt < MAX_CNT:
            MAX_CNT = cnt
            return
    
    for i in range(N-1):
        for j in range(i+1, i+k+1):
            if j < N:  # swap할 idx가 n보다 작으면
                if swap(arr, i, j):  # swap 하였으면
                    m_sort(arr, cnt+1, k)
                    arr[i], arr[j] = arr[j], arr[i]


arr = [2,1,3,4,5]
k = 3
solution(arr, k)
print(MAX_CNT)