# 백준 1780번 S2
# 종이의 개수

# 전체를 검사
# 첫번째 값을 flag에 저장 >> 다른 값이 나오면 나누기
# 같은 값이면 cnt += 1
# n의 8방 dx, dy 설정하여 i, j 값을 초기화

import sys

input = sys.stdin.readline

def check(_li):
    _n = len(_li)
    num = 0
    for i in range(_n):
        for j in range(_n):
            if i == 0 and j == 0:
                num = _li[i][j]
            else:
                if _li[i][j] != num:
                    return False
    return num


def my_divide(_li, _n):
    global cnt_0, cnt_1, cnt_m1

    if _n == 1:
        num = _li[0][0]
        if num == 0:
            cnt_0 += 1
        elif num == 1:
            cnt_1 += 1
        else:
            cnt_m1 += 1
    else:
        flag = check(_li)
        if flag is False:
            _n = _n // 3
            
            # 9개로 나눔
            di = [0, 0, 0, _n, _n, _n, _n*2, _n*2, _n*2]
            dj = [0, _n, _n*2, 0, _n, _n*2, 0, _n, _n*2]

            for i in range(9):
                # 새로운 배열 생성
                _i = di[i]
                _j = dj[i]
                
                new_li = []
                for k in range(_i, _i+_n):
                    tmp_li = []
                    for l in range(_j, _j+_n):
                        tmp_li.append(_li[k][l])
                    new_li.append(tmp_li)
                
                my_divide(new_li, _n)
        else:  # 나누지 않아도 된다면
            if flag == 0:
                cnt_0 += 1
            elif flag == 1:
                cnt_1 += 1
            else:
                cnt_m1 += 1


n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

cnt_0 = 0
cnt_1 = 0
cnt_m1 = 0

my_divide(li, n)

print(cnt_m1)
print(cnt_0)
print(cnt_1)

