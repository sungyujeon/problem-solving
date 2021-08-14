# 간식의 개수


def count_snack(secs, time, cnt):
    share = secs // time
    _remain = 0

    if share > cnt:
        _remain = secs - (time * cnt)
        share = cnt
    else:
        _remain = secs % time

    return (_remain, share)


def solution(seconds):
    total = 0
    remain = seconds
    snack_list = [(300, 10), (130, 30), (120, 20), (20, 30)]

    for times, cnts in snack_list:
        res = count_snack(remain, times, cnts)
        remain = res[0]
        total += res[1]

    return total


seconds = 460
print(solution(seconds))
