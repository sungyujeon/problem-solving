# greedy
# 현재 상황의 최적해로 계산하였을 때 해가 나오는 문제일 때 적용 가능

#1 동전 문제
def solution1(n):
    count = 0
    coins = [500, 100, 50, 10]
    for coin in coins:
        count += n // coin
        n %= coin
    return count

N = 1260
coins = [500, 100, 50, 10]
print(solution1(N))


#2 1이 될 때까지
# N-1 or N / K 둘 중에 하나로 1을 만드는 최소 횟수
# 아래 풀이보다 최적화 가능
def solution2(N, K):
    cnt = 0
    while N != 1:
        if N % K == 0:
            N //= K
        else:
            N -= 1
        cnt += 1
    return cnt
        

N, K = 25, 5
print(solution2(N, K))

#3 곱하기 혹은 더하기
# 02984 576
def solution3(string):
    arr = list(map(int, list(string)))
    res = 0
    
    for num in arr:
        if res <= 1 or num <= 1:
            res += num
        else:
            res *= num
    return res

string = '02984'
print(solution3(string))


#4 모험가 길드

def solution4(N, arr):
    # groups = 0
    # arr.sort(reverse=True)
    # rear = 0

    # while rear < N:
    #     curr = arr[rear]
    #     rear += curr
    #     groups += 1
    # return groups
    res = 0
    cnt = 0

    for i in arr:
        cnt += 1
        if cnt >= arr[i]:
            res += 1
            cnt = 0

N = 5
X = [2, 3, 1, 2, 2]
print(solution4(N, X))

