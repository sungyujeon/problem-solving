import sys

sys.stdin = open('input.txt', 'r')

def dfs(arr):
    visited = [[False] * n for _ in range(n)]
 
    res_xy = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                if arr[i][j]:  # 용기가 있으면
                    nx = j + 1
                    ny = i + 1
                    end_x_idx = j
                    end_y_idx = i
 
                    while nx < n and arr[i][nx]:
                        visited[i][nx] = True
                        end_x_idx += 1
                        nx += 1
 
                    while ny < n and arr[ny][j]:
                        for k in range(j, end_x_idx+1):
                            visited[ny][k] = True
                        end_y_idx += 1
                        ny += 1
 
                    res_xy.append([end_y_idx-i+1, end_x_idx-j+1])
 
    return res_xy
 
 
T = int(input())
 
for tc in range(1, T+1):
    n = int(input())
    containers = [list(map(int, input().split())) for _ in range(n)]
 
    result_list = dfs(containers)
 
    # 크기/행 순으로 정렬
    result_list.sort(key=lambda x: (x[0] * x[1], x[0]))
 
    res_cnt = len(result_list)
 
    print(f'#{tc} {res_cnt}', end=' ')
    for i in result_list:
        print(i[0], i[1], end=' ')
    print()