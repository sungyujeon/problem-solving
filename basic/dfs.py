# dfs
# 탐색(Search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
# stack
# - 탐색 시작 노드를 스택에 삽입하고 방문 처리
# - 스택이 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
# - 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

#1 factorial
# memoization으로 계산 caching 가능
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n-1)

print(factorial(10))

#2 유클리드 호제법
def gcd(a, b):
    if a % b == 0:
        return b
    
    return gcd(b, a % b)

print(gcd(192, 162))




#1 음료수 얼려 먹기
# N x M 얼음틀
# 구멍:0, 칸막이:1
# 얼음틀 모양이 주어졌을 때 생성되는 총 아이스크림 개수
# N = 4, M = 5 => 3
def dfs(cij, arr, visited, N, M):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    ci, cj = cij

    for k in range(4):
        ni = ci + di[k]
        nj = cj + dj[k]
        
        if 0 <= ni < N and 0 <= nj < M:
            if not visited[ni][nj] and arr[ni][nj] == 0:
                visited[ni][nj] = True
                dfs((ni, nj), arr, visited, N, M)



def solution1(N, M, arr):
    res = 0
    arr = list(map(lambda x: list(map(int, list(x))), arr))
    visited = [[False for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and not visited[i][j]:
                dfs((i, j), arr, visited, N, M)
                res += 1
    return res

N, M = 4, 5  # 1 <= N, M <= 1000
arr = ['00110', '00011', '11111', '00000']
print(solution1(N, M, arr))