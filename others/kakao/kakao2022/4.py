# 카카오블라인드 2022 4번
from pprint import pprint


def dfs(curr, remain, myTotal, yourTotal, info, myInfo, myMax, res):
    if curr == 11 or remain == 0:
        # 어피치 계산 전
        if curr < 11:
            for i in range(curr, 11):
                if info[i] != 0:
                    yourTotal += (10-i)
        diff = myTotal - yourTotal
        if diff <= 0:  # 짐
            pass
        else:  # 이김
            if diff >= myMax:
                if diff > myMax:
                    res = [myInfo]
                    myMax = diff
                else:
                    res.append(myInfo)
        return [myMax, res]

    yCnt = info[curr]
    if (yCnt+1) <= remain:
        info1 = [*myInfo]
        info1[curr] = yCnt + 1
        [myMax, res] = dfs(curr+1, remain-(yCnt+1), myTotal +
                           (10-curr), yourTotal, info, info1, myMax, res)

    for i in range(yCnt+1):
        info2 = [*myInfo]
        if i <= remain:
            info2[curr] = i
            [myMax, res] = dfs(curr+1, remain-i, myTotal, yourTotal +
                               (10-curr), info, info2, myMax, res)
    return [myMax, res]


def solution(n, info):
    res = []
    remain = n
    myInfo = [0 for _ in range(11)]

    [myMax, res] = dfs(0, remain, 0, 0, info, myInfo, 0, res)
    res.sort(key=lambda x: (x[10], x[9], x[8], x[7],
             x[6], x[5], x[4], x[3], x[2], x[1], x[0]))

    if res:
        return res[-1]
    return [-1]


n = 10
info = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(solution(n, info))
