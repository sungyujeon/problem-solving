# 삼성 소프트웨어 역량테스트 모의 A형
# 2번

def getCost(a, b, c, d, arr):
    cost1 = ((arr[a] + arr[b]) ** 2) + ((arr[c] + arr[d]) ** 2)
    cost2 = ((arr[a] + arr[d]) ** 2) + ((arr[b] + arr[c]) ** 2)
    return max(cost1, cost2)

T = int(input())
for t in range(1, T+1):
    res = 0
    N = int(input())
    arr = list(map(int, input().split()))


    for i in range(N-6):
        if i == 0:
            for j in range(i+2, N-5):
                for k in range(j+2, N-3):
                    for l in range(k+2, N-1):
                        cost = getCost(i, j, k, l, arr)

                        if cost > res:
                            res = cost
        else:
            for j in range(i+2, N-4):
                for k in range(j+2, N-2):
                    for l in range(k+2, N):
                        cost = getCost(i, j, k, l, arr)

                        if cost > res:
                            res = cost

    print("#%d %d" % (t, res))