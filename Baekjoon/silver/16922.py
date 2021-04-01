# 백준 16922번 S3
# 로마 숫자 만들기

import sys
input = sys.stdin.readline

n = int(input())

sum_set = set()
for i in range(n+1):
    for j in range(n-i+1):
        for k in range(n-i-j+1):
            t = n - i - j - k
            total = i * 1 + j * 5 + k * 10 + t * 50
            sum_set.add(total)

print(len(sum_set))



# sum_set = set()
# def dfs(depth, _n, _sum):
#     global sum_set

#     if depth == _n:
#         sum_set.add(_sum)
#         return

#     dfs(depth+1, _n, _sum+1)
#     dfs(depth+1, _n, _sum+5)
#     dfs(depth+1, _n, _sum+10)
#     dfs(depth+1, _n, _sum+50)


# stack = [1, 5, 10, 50]

# dfs(1, n, 1)
# dfs(1, n, 5)
# dfs(1, n, 10)
# dfs(1, n, 50)

# print(len(sum_set))
