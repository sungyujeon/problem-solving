# 라인 공채 2021 2번

# 전월 사용자의 검색기록 일기준 research
# 일기준 몇 번 검색되었는지 정리
# 연속된 n일 동안 매일 최소 k번 이상 검색 + 총 2nk 이상 검색 -> 이슈검색어
# 이슈 검색어 중 가장 여러 번 이슈 검색어가 된 검색어 -> 최고의 이슈 검색어
# 여러 개일 경우 사전 순
# 없으면 None 리턴

def setArray(array):
    n = len(array)
    researchDict = {}

    for i in range(n):
        words = array[i]
        for word in words:
            w = researchDict.get(word)
            if w == None:
                researchDict[word] = [0 for _ in range(n)]
                researchDict[word][i] += 1
            else:
                researchDict[word][i] += 1

    return researchDict


def calcKeyword(arr, n, k):
    _len = len(arr)
    K = 2 * n * k

    total = 0
    start = 0
    end = n

    while end <= _len:
        # check
        tmpFlag = True
        tmpTotal = 0
        for i in range(start, end):
            tmpTotal += arr[i]
            if arr[i] < k:
                tmpFlag = False

        if tmpTotal >= K and tmpFlag:
            total += 1

        start += 1
        end += 1

    return total


def getKeyword(researchDict, n, k):
    keywordList = []
    for key in researchDict.keys():
        arr = researchDict.get(key)
        total = calcKeyword(arr, n, k)
        keywordList.append([key, total])

    return keywordList


def solution(research, n, k):
    researchDict = setArray(research)
    keywordList = getKeyword(researchDict, n, k)

    keywordList.sort(key=lambda x: (x[0], x[1]))
    keywordList.sort(key=lambda x: x[1], reverse=True)
    print(keywordList)

    if keywordList[0][1] < 1:
        return 'None'
    else:
        res = keywordList[0][0]
        return res


research = ["abaaaa", "aaa", "abaaaaaa", "fzfffffffa"]
n = 2
k = 2
print(solution(research, n, k))
