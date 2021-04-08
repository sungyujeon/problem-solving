def l(num):
    d1 = num // 1000
    num %= 1000
    d2 = num // 100
    num %= 100
    d3 = num // 10
    num %= 10
    d4 = num

    num = [d2, d3, d4, d1]
    num = list(map(str, num))
    num = int(''.join(num))

    return num


n = 12
res = l(n)
print(res)