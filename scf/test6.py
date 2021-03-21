
# sys.stdin = open('input.txt', 'r')
import sys
input = sys.stdin.readline

def bfs(_li):
    global n, m

    visited = [[False] * m for _ in range(n)]

    stack = [[(0,0)]]
    while stack:
        tmp = stack.pop()    
        
        tmp_stack = []
        for _ in range(len(tmp)):
            i, j = tmp.pop()

            if not visited[i][j]:
                visited[i][j] = True
                
                if i > 0 and j > 0:
                    _li[i][j] += max(_li[i-1][j], _li[i][j-1])
                else:
                    if i != 0 or j != 0:
                        if i == 0:
                            _li[i][j] += _li[i][j-1]
                        else:
                            _li[i][j] += _li[i-1][j]

                for k in [(0, 1), [1, 0]]:
                    ni = i + k[0]
                    nj = j + k[1]
                    
                    if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                        tmp_stack.append((ni, nj))
        if tmp_stack:
            stack.append(tmp_stack)


m, n = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

bfs(li)

print(li[n-1][m-1])