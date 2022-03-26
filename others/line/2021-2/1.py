# 라인 2021 공채 1번


def getCount(start, end, student):
    startK = 1
    endK = 1
    startIdx = 0

    for i in range(start, end+1):
        if student[i] == 1:
            startIdx = i+1
            break
        startK += 1

    for i in range(end+1, len(student)):
        if student[i] == 1:
            nextIdx = i
            break
        endK += 1

    return (startK, endK, startIdx)


def solution(student, k):
    n = len(student)
    res = 0
    start = 0
    end = 0

    ks = student[0]
    while end < n:
        if ks < k:
            end += 1
            if end == n:
                break
            ks += student[end]
        elif ks == k:
            s, e, si = getCount(start, end, student)
            res += s * e
            start = si
            ks -= 1

    return res


student = [0, 1, 0, 1]
k = 2
print(solution(student, k))
