def divisor(n):
    total = 0
    for j in range(1, n+1):
        if not n % j:
            total += 1

    r = False
    if not total % 2:
        r = True
    
    return r


left = 13
right = 17

res = 0
for i in range(left, right+1):
    if divisor(i):
        res += i
    else:
        res -= i

print(res)
