# 백준 2630번 S3
# 색종이 만들기

import sys

input = sys.stdin.readline

def isCut(arr, n):
    for i in range(n):
        for j in range(n):
            if not arr[i][j]:
                return False
    return True

def isWhiteCut(arr, n):
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                return False
    return True

def quadrant(arr, n):
    # 각 사분면 새로운 배열 생성
    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []
    
    n2 = n // 2
    for i in range(n):
        tmp_arr1 = []
        tmp_arr2 = []
        tmp_arr3 = []
        tmp_arr4 = []

        for j in range(n):
            if 0 <= i < n2: # 세로로 반 위
                if 0 <= j < n2:  # 2사분면
                    tmp_arr2.append(arr[i][j])
                else:  # 1사분면
                    tmp_arr1.append(arr[i][j])
            else:  # 세로로 반 아래
                if 0 <= j < n2:  # 3사분면
                    tmp_arr3.append(arr[i][j])
                else:  # 4사분면
                    tmp_arr4.append(arr[i][j])
        
        if tmp_arr1:
            arr1.append(tmp_arr1)
            arr2.append(tmp_arr2)
        else:
            arr3.append(tmp_arr3)
            arr4.append(tmp_arr4)

    return (arr1, arr2, arr3, arr4)

def cut(arr, n):
    cnt = 0
    white_cnt = 0

    if isCut(arr, n):
        cnt += 1
    elif isWhiteCut(arr, n):
        white_cnt += 1
    else:
        if not n // 2:  # n == 1이면
            if arr[0][0]:
                cnt += 1
            else:
                white_cnt += 1
        else:
            quadrant_tuple = quadrant(arr, n)
            arr1 = quadrant_tuple[0]
            arr2 = quadrant_tuple[1]
            arr3 = quadrant_tuple[2]
            arr4 = quadrant_tuple[3]
            
            # n초기화
            n = n // 2
            
            # 각 사분면 종이 cnt
            cnt_tuple1 = cut(arr1, n)
            cnt_tuple2 = cut(arr2, n)
            cnt_tuple3 = cut(arr3, n)
            cnt_tuple4 = cut(arr4, n)
            
            cnt += cnt_tuple1[0] + cnt_tuple2[0] + cnt_tuple3[0] + cnt_tuple4[0]
            white_cnt += cnt_tuple1[1] + cnt_tuple2[1] + cnt_tuple3[1] + cnt_tuple4[1]
    return (cnt, white_cnt)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

cut_tuple = cut(arr, n)
print(cut_tuple[1])
print(cut_tuple[0])