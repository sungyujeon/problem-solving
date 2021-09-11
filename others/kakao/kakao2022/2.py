# 카카오 블라인드 2022 2번

def setNotation(num, base):
    if num < base:
        return str(num)

    res = ''
    while num // base >= 1:
        remain = num % base
        num //= base
        res = str(remain) + res
        if num < base:
            res = str(num) + res

    return res


def isPrime(x):
    if x == 1:
        return False

    for i in range(2, int(x ** (1/2)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    res = 0
    n = setNotation(n, k)
    N = len(n)

    i = 0
    tmp = ''
    while i <= N:
        if i == N:
            if tmp:
                tmp = int(tmp)
                if isPrime(tmp):
                    res += 1
            break

        c = n[i]
        if c != '0':
            tmp += c
            i += 1
        else:  # 0이면
            if tmp:
                tmp = int(tmp)
                flag = isPrime(tmp)
                if flag:
                    res += 1
                tmp = ''
            i += 1
    return res


n = 3
k = 3
print(solution(n, k))
