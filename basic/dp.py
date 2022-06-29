# dynamic programming
# 메모리를 적절히 사용해 수행시간 효율성을 비약적으로 향상시키는 방법
# 이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장해 다시 계산하지 않는 것(memoization)

#1 개미 전사
# 붙어 있는 식량창고는 약탈이 불가능, 식량창고 N 정보 주어지면 얻을 수 있는 식량 최댓값
# 식량창고 갯수 3 <= N <= 100, 식량개수 0 <= K <= 1000

def solution1(N, arr):
    arr[2] += arr[0]
    for i in range(3, N):
        arr[i] = max((arr[i] + arr[i-2]), (arr[i] + arr[i-3]))

    return max(arr[N-1], arr[N-2])

def other_solution1(N, arr):
    dp = [0] * N
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for k in range(2, N):
        dp[k] = max(dp[k-1], dp[k-2] + arr[k])
    
    return dp[N-1]
N = 5
arr = [1, 3, 1, 5, 100]  # => 103
# print(solution1(N, arr))
# print(other_solution1(N, arr))


#2 1로 만들기
# 정수 x에 4가지 연산
# x가 5로 나누어떨어지면 5로 나눔, 3으로 나누어떨어지면 3으로 나눔, 2로 나누어떨어지면 2로 나눔, x에서 1을 뺌
# 정수 x가 주어졌을 때 연산 4개로 1을 만들 때, 연산 사용 최수 횟수
# 1 <= x <= 30,000

def solution2(x):
    dp = [0] * 30001

    for i in range(2, x + 1):
        dp[i] = dp[i-1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i // 5] + 1)
    
    return dp[x]

x = 26  #=> 3
# print(solution2(x))


#3 효율적인 화폐 구성
# N 종류의 화폐, 개수를 최소한으로 해서 그 가치의 합이 M원이 되도록, 못 만들 시 -1
# 1 <= N <= 100, 1 <= M <= 10000

def solution3(N, M, arr):
    dp = [-1] * (M+1)
    dp[0] = 0
    min_value = min(arr)
    
    for k in range(min_value, M+1):
        tmp = 10001
        for coin in arr:
            if k - coin >= 0:
                prev = dp[k-coin]
                if prev != -1 and prev < tmp:
                    dp[k] = dp[k-coin] + 1
    
    return dp[M]
    

# N, M = 2, 15 # => 5
N, M = 3, 4 # => -1
# arr = [2, 3]
arr = [3, 5, 7]
# print(solution3(N, M, arr))



#4 금광
# n * m 금광
# 어떤 열에서도 출발할 수 있고, m-1번에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래 중 한군데로 이동할 수 있음
# 얻을 수 있는 금의 최대 크기
from pprint import pprint

def solution4(N, M, arr):
    dp = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(1):
            dp[i][j] = arr[i][j]


    for j in range(1, M):  # 각 행에서 시작
        for i in range(N):
            judge(i, j, dp, arr, N, M)
    
    max_value = 0
    for i in range(N):
            if dp[i][M-1] > max_value:
                max_value = dp[i][M-1]
    pprint(dp)
    
    return max_value

def judge(i, j, dp, arr, N, M):
    max_value = 0
    d = [(-1, -1), (0, -1), (1, -1)]
    
    for k in range(3):
        pi = i + d[k][0]
        pj = j + d[k][1]

        if 0 <= pi < N and 0 <= pj < M:
            r = arr[i][j] + dp[pi][pj]
            if r > max_value:
                max_value = r
    
    dp[i][j] = max_value
        

N, M = 3, 4
arr = [
    [1, 3, 3, 2],
    [2, 1, 4, 1],
    [0, 6, 4, 7]
]
print(solution4(N, M, arr))



#5 병사 배치하기
# N명의 병사 무작위 나열 -> 전투력 높은 병사가 앞에 오도록 내림차순 배치
# 남아 있는 병사의 수가 최대가 되도록 열외시켜야 하는 병사의 수
# 1 <= N < 2000, 전투력 <= 10,000,000
# LIS(Longest Increasing Subsequence)

def solution5(N, arr):
    arr.reverse()
    dp = [1] * N

    for i in range(1, N):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return N - max(dp)
        
N = 7
arr = [15, 11, 4, 8, 5, 2, 4]
print(solution5(N, arr))
