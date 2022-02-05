# 백준 1337번
# 올바른 배열

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

def solution(N):
    global arr, n

    res = N-1
    curr = N-1
    front = 0
    rear = 0
    while front != n:
        if rear == front:
            if curr > N-1:
                curr = N-1
            rear += 1
            continue
        
        if rear == n or rear - front == N:
            break

        frontValue = arr[front]
        rearValue = arr[rear]
        maxValue = frontValue + (N-1)

        if rearValue <= maxValue:
            curr -= 1
            rear += 1
            res = curr if curr < res else res
        else:
            curr += 1
            front += 1

    return res

N = 5
print(solution(N))


# res = 4
# curr = 4
# front = 0
# back = 0
# while front != n:
#     frontValue = arr[front]
#     backValue = arr[back]

#     diff = backValue - frontValue

#     if diff == 0:
#         front = back
#         back += 1
#         curr = 4
#         continue
    
#     if diff == 1:
#         curr -= 1
#         changeResult(curr)
#         front = back
#         back += 1
    