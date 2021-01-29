# 백준 9184번
# Function Run Fun

mem = {}

def dp(a, b, c):
    global mem

    if (a, b, c) in mem:
        return mem[(a, b, c)]
    else:
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        elif a > 20 or b > 20 or c > 20:
            mem[(20, 20, 20)] = dp(20, 20, 20)
            return mem[(20, 20, 20)]
        elif a < b and b < c:
            mem[(a, b, c)] = dp(a, b, c-1) + dp(a, b-1, c-1) - dp(a, b-1, c)
            return mem[(a, b, c)]
        else:
            mem[(a, b, c)] = dp(a-1, b, c) + dp(a-1, b-1, c) + dp(a-1, b, c-1) - dp(a-1, b-1, c-1)
            return mem[(a, b, c)]

while True:
    a, b, c = map(int, input().split())
    if [a, b, c] == [-1, -1, -1]:
        break
    
    print('w({0}, {1}, {2}) = {3}'.format(a, b, c, dp(a, b, c)))
    