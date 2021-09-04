# 2020 카카오 블라인드
# 문자열 압축


def getComp(s, r):
    n = len(s)
    start = 0
    end = r

    total = n
    cnt = 1
    curr_s = ''

    while (end <= n):
        next_s = s[start:end]

        if curr_s == next_s:
            cnt += 1
        else:
            if (cnt != 1):
                _cnt = str(cnt)
                total += len(_cnt)
            cnt = 1
            curr_s = next_s

        if (cnt != 1):
            total -= r

        start += r
        end += r

        if (cnt > 1 and end > n):
            _cnt = str(cnt)
            total += len(_cnt)

    return total


def solution(s):
    n = len(s)
    if n == 1:
        return 1

    res = n + 1
    r = 0

    for i in range(n-1, 0, -1):
        length = getComp(s, i)

        if (length < res):
            res = length
    return res


s = "xxxxxxxxxxyyy"
print(solution(s))
