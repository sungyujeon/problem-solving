# 2021 카카오 채용연계형 인턴십 3번
# 표 편집

# def onUp(curr, cnt, exists):
#     total = 0
#     for i in range(curr-1, -1, -1):
#         if exists[i]:
#             total += 1
#             if total == cnt:
#                 return i


# def onDown(curr, cnt, exists, n):
#     total = 0
#     for i in range(curr+1, n):
#         if exists[i]:
#             total += 1
#             if total == cnt:
#                 return i


# def getDeletedNextIdx(curr, exists, n):
#     for i in range(curr, n):
#         if exists[i]:
#             return i

#     for i in range(curr, -1, -1):
#         if exists[i]:
#             return i


# def solution(n, k, cmd):
#     exists = [True] * n
#     deleted = []
#     curr = k

#     for c in cmd:
#         if c[0] in ['D', 'U']:
#             command = c[0]
#             cnt = int(c[-1])

#             if c[0] == 'D':
#                 curr = onDown(curr, cnt, exists, n)
#             else:
#                 curr = onUp(curr, cnt, exists)
#         else:
#             command = c
#             if c == 'Z':
#                 if deleted:
#                     idx = deleted.pop()
#                     exists[idx] = True
#             else:  # 삭제
#                 exists[curr] = False
#                 deleted.append(curr)
#                 idx = getDeletedNextIdx(curr, exists, n)
#                 curr = idx

#     res = ''
#     for f in exists:
#         if f:
#             res += 'O'
#         else:
#             res += 'X'
#     return res

def binarySearch(arr, target):
    if not arr:
        return

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        l = arr[left]
        r = arr[right]
        m = arr[mid]

        if target < m:
            right = mid - 1
        else:
            left = mid + 1
    return left


def solution(n, k, cmd):
    idxs = [i for i in range(n)]
    deleted = []
    curr = k

    for c in cmd:
        if c[0] in ['D', 'U']:
            command, cnt = c.split()
            cnt = int(cnt)
            if command == 'D':
                curr += cnt
            else:
                curr -= cnt
        else:
            if c == 'Z':
                if deleted:
                    dIdx = deleted.pop()
                    idxs.insert(binarySearch(idxs, dIdx), dIdx)
                    if idxs[curr] > dIdx:
                        curr += 1
            else:  # 삭제
                if curr == len(idxs) - 1:
                    deleted.append(idxs.pop())
                    curr -= 1
                else:
                    deleted.append(idxs.pop(curr))

    res = ['O'] * n
    for i in deleted:
        res[i] = 'X'

    return ''.join(res)


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
print(solution(n, k, cmd))
