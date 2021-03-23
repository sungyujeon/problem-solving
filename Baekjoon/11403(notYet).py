# 백준 11403번 S1
# 경로 찾기(플로이드 와샬 알고리즘)

# 경로 n 반복문
# n으로 갈 수 있는 list만큼 이중 반복
# visited 초기화
# visited[n] = 1
# stack.append(j)
# cnt_flag = False

# while stack
# stack.pop() >> nodes 반복
# if tmp_cnt and node == i: [n][n] == 1 return
# else
# if node not visited: visited check and append stack the j's nodes
# if not cnt_flag: cnt_flag = True

import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, j, li, res, n):
    visited = [False] * n
    visited[i] = True
    
    cnt_flag = False
    stack = [j]

    while stack:
        node = stack.pop()
        res[i][node] = 1
        visited[node] = True
        
        for k in range(n):
            if res[node][k]:
                if cnt_flag and k == i:
                    res[i][i] = 1
                if not visited[k]:
                    stack.append(k)

        if not cnt_flag:
            cnt_flag = True
    
    return False


n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

# 경로 초기화
res = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if li[i][j]:
            res[i][j] = 1
            res[j][i] = 1

for i in range(n):
    for j in range(n):
        if res[i][j]:
            tmp_flag = dfs(i, j, li, res, n)
            if tmp_flag:
                break

print(res)
