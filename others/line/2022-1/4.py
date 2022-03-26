def solution(arr, brr):
    answer = 0
    N = len(arr)
    
    for i in range(N-1):
        start, end = arr[i], brr[i]
        if start == end:
            continue
        
        diff = end - start
        arr[i] += diff
        arr[i+1] -= diff
        answer += 1
        
    return answer

arr = [3, 7, 2, 4]
brr = [4, 5, 5, 2]
print(solution(arr, brr))