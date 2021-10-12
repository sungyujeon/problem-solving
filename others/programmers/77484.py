# 프로그래머스 2021 데브매칭 상반기
# 로또의 최고 순위와 최저 순위

def getRank(num):
    res = 6

    if num == 6:
        res = 1
    elif num == 5:
        res = 2
    elif num == 4:
        res = 3
    elif num == 3:
        res = 4
    elif num == 2:
        res = 5

    return res


def solution(lottos, win_nums):
    cnt = 0
    zero_cnt = 0

    for num in lottos:
        if num == 0:  #
            zero_cnt += 1
        else:
            if num in win_nums:
                cnt += 1

    minimum = cnt
    maximum = cnt + zero_cnt

    return [getRank(maximum), getRank(minimum)]


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))
