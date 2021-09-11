# 카카오 블라인드 2022 1번


def setReported(reported, reportedFrom, k):
    for value in reportedFrom.values():
        for v in value:
            reported[v] += 1

    li = []
    for key, value in reported.items():
        if value >= k:
            li.append(key)
    return li


def solution(id_list, report, k):
    n = len(id_list)
    res = [0] * n
    reportedFrom = {}
    reported = {}

    for myId in id_list:
        reportedFrom[myId] = set([])
        reported[myId] = 0

    for r in report:
        rFrom, rTo = r.split()
        reportedFrom.get(rFrom).add(rTo)

    reportedList = setReported(reported, reportedFrom, k)
    for idx, value in enumerate(reportedFrom.values()):
        for item in reportedList:
            if item in value:
                res[idx] += 1
    return res


id_list = ["muzi", "frodo", "apeach", "neo"]
id_list = ["con", "ryan"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, report, k))
