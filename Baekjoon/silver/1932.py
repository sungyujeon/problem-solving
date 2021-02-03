# 백준 1932번 S1
# 정수 삼각형
import sys

n = int(sys.stdin.readline())

tri_list = []
for _ in range(n):
    tri_list_tmp = list(map(int, sys.stdin.readline().split()))
    tri_list.append(tri_list_tmp)

for i in range(len(tri_list)):
    if n == 1:
        print(tri_list[0])
        break
    elif i != n -1:
        for j in range(len(tri_list[i+1])):
            if j == 0:
                tri_list[i+1][j] += tri_list[i][j]
            elif j == len(tri_list[i+1]) - 1:
                tri_list[i+1][j] += tri_list[i][j-1]
            else:
                tri_list[i+1][j] = max(tri_list[i+1][j] + tri_list[i][j-1], tri_list[i+1][j] + tri_list[i][j])
        if i == n - 1:
            break
print(max(tri_list[len(tri_list) - 1]))