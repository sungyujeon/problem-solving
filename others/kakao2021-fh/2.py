# 카카오 블라인드 2021 하반기
# 메뉴 리뉴얼

def comb(s, n, resDict):

    def dfs(s, i, depth, n, rs, resDict):
        if depth == n:
            if resDict[n].get(rs) == None:
                resDict[n][rs] = 1
            else:
                resDict[n][rs] += 1
            return

        for k in range(i, len(s) - n + depth + 1):
            dfs(s, k+1, depth+1, n, rs+s[k], resDict)

    dfs(s, 0, 0, n, '', resDict)


def solution(orders, course):
    resDict = {}
    for num in course:
        resDict[num] = {}

    for num in course:
        for order in orders:
            tmpOrder = sorted(list(order))
            if len(order) >= num:
                comb(tmpOrder, num, resDict)

    res = []
    for num in course:
        resDict[num] = sorted(resDict[num].items(), key=lambda x: (
            x[1], x[0]), reverse=True)

        tmpMax = 2
        for item in resDict[num]:
            if item[1] >= tmpMax:
                tmpMax = item[1]
                res.append(item[0])
            else:
                break

    res.sort()

    return res


orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
print(solution(orders, course))
