# 백준 2559번 S3
# 수열

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
temp_list = list(map(int, input().split()))

max_temp = sum(temp_list[:k])
if k == 1:
    print(max(temp_list))
else:
    tmp_sum = max_temp
    i = 0
    while i + k < n:
        tmp_sum -= temp_list[i]
        tmp_sum += temp_list[i+k]

        if tmp_sum > max_temp:
            max_temp = tmp_sum

        i += 1

    print(max_temp)