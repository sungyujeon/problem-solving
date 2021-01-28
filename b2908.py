# 백준 2908번
# 상수

a, b = map(int, input().split())

def num_rev(number):
    return int(''.join(reversed(list(str(number)))))

a_rev = num_rev(a)
b_rev = num_rev(b)

def check(a, b):
    return a if a > b else b

print(check(a_rev, b_rev))