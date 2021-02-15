# 백준 1959번 G2
# 달팽이3
import sys

input = sys.stdin.readline

m, n = map(int, input().split())

i = j = 0


arr = [[0] * n for _ in range(m)]
num = 0
cnt = 0
dir = [(0,1), (1,0), (0,-1), (-1,0)]
while True:
    if 0 <= i <=m-1 and 0 <= j <= n-1 and arr[i][j] == 0:
        arr[i][j] = 1
        i += dir[0][0]
        j += dir[0][1]
        num += 1
    else:
        i -= dir[0][0]
        j -= dir[0][1]

        dir.append(dir.pop(0))
        cnt += 1
        i += dir[0][0]
        j += dir[0][1]
    
    if num == m * n:
        i -= dir[0][0]
        j -= dir[0][1]
        break

print(cnt)
print(i+1, j+1)

        
        