# 백준 1629번 S1
# 곱셈 / 분할정복

import sys
input = sys.stdin.readline

def conq(_a, _b, _c):
    if _b == 1:
        return _a % _c
    else:
        tmp = conq(_a, _b // 2, _c)
        
        if _b % 2:  # 홀수이면
            return ((tmp ** 2) * _a) % _c
        else:
            return (tmp ** 2) % _c

a, b, c = map(int, input().split())

res = conq(a, b, c)
print(res)


# multiple = _dp.get(div)
# if n % 2:  # 홀수 제곱수
#     num = (multiple ** 2) * num
# else:  # 짝수 제곱수
#     num = multiple ** 2

# return num % _c