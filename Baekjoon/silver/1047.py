# 백준 1047번 S1
# Z
import sys

input = sys.stdin.readline

def z(_n, _r, _c):
    if _n == 1:
        return 1

    # 초기화
    res = 0
    mid = _n // 2

    if _r < mid and _c < mid:  # 2사분면
        res += z(mid, _r, _c)
    elif _r < mid and mid <= _c < n:  # 1사분면
        _c -= mid
        res += mid ** 2
        res += z(mid, _r, _c)
    elif mid <= _r < n and _c < mid:  # 3사분면
        _r -= mid
        res += 2 * (mid ** 2)
        res += z(mid, _r, _c)
    else:  # 4사분면
        _r -= mid
        _c -= mid
        res += 3 * (mid ** 2)
        res += z(mid, _r, _c)
    
    return res


n, r, c = map(int, input().split())
n = 2 ** n
result = z(n, r, c)

print(result-1)
