# 카카오블라인드 2021
# 순위검색

from pprint import pprint


def setQueries(query):
    for i in range(len(query)):
        query[i] = query[i].replace(' and', '').split(' ')


def setInfo(info):
    n = len(info)
    infos = [[]] * n
    for i in range(len(info)):
        infos[i] = info[i].split(' ')
    return infos


def setDatas(infos):
    datas = {
        'java': {
            'backend': {
                'junior': {
                    'pizza': [],
                    'chicken': []
                },
                'senior': {
                    'pizza': [],
                    'chicken': []
                }
            },
            'frontend': {
                'junior': {
                    'pizza': [],
                    'chicken': []
                },
                'senior': {
                    'pizza': [],
                    'chicken': []
                }
            }
        },
        'python': {
            'backend': {
                'junior': {
                    'pizza': [],
                    'chicken': []
                },
                'senior': {
                    'pizza': [],
                    'chicken': []
                }
            },
            'frontend': {
                'junior': {
                    'pizza': [],
                    'chicken': []
                },
                'senior': {
                    'pizza': [],
                    'chicken': []
                }
            }
        },
        'cpp': {
            'backend': {
                'junior': {
                    'pizza': [],
                    'chicken': []
                },
                'senior': {
                    'pizza': [],
                    'chicken': []
                }
            },
            'frontend': {
                'junior': {
                    'pizza': [],
                    'chicken': []
                },
                'senior': {
                    'pizza': [],
                    'chicken': []
                }
            }
        }
    }

    for inf in infos:
        [a, b, c, d, score] = inf
        datas.get(a).get(b).get(c).get(d).append(int(score))

    return datas


def sortDatas(depth, datas):
    if depth == 4:
        datas.sort(reverse=True)
        return

    for key in datas.keys():
        sortDatas(depth+1, datas.get(key))


def getIndex(arr, qScore):
    if not arr:
        return 0

    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2

    while left <= right:
        mid = (left + right) // 2
        l = arr[left]
        r = arr[right]
        m = arr[mid]
        if m == qScore:
            while mid < len(arr) and arr[mid] == qScore:
                mid += 1
            return mid

        if m > qScore:
            left = mid + 1
        else:
            right = mid - 1

    return left


def dfs(qs, depth, currDatas):
    if depth == 4:
        qScore = int(qs[4])
        return getIndex(currDatas, qScore)

    _tmp = 0
    if qs[depth] == '-':
        for key in currDatas.keys():
            _tmp += dfs(qs, depth+1, currDatas.get(key))
        return _tmp
    else:
        return dfs(qs, depth+1, currDatas.get(qs[depth]))


def getQuery(q, datas):
    total = 0
    total += dfs(q, 0, datas)

    return total


def solution(info, query):
    res = []
    setQueries(query)
    infos = setInfo(info)
    datas = setDatas(infos)
    sortDatas(0, datas)

    for q in query:
        res.append(getQuery(q, datas))

    return res


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]

print(solution(info, query))
