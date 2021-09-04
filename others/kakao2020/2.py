# 2020 카카오 블라인드
# 괄호 변환

def isRight(s):
    arr = []

    for i in s:
        if i == '(':
            arr.append(i)
        else:
            if not arr:
                return False
            else:
                arr.pop()

    return True


def divide(s):
    left = 0
    right = 0

    if not s:
        return ''

    u = ''
    v = ''
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        else:
            right += 1

        if left == right:
            u = s[:i+1]
            v = s[i+1:]
            break

    if (isRight(u)):
        u += divide(v)
        return u
    else:
        tmp = '('
        tmp += divide(v)
        tmp += ')'
        uTmp = u[1:-1]
        t = ''
        for i in range(len(uTmp)):
            if uTmp[i] == '(':
                t += ')'
            else:
                t += '('
        tmp += t
        return tmp


def solution(p):
    answer = ''

    flag = isRight(p)
    if flag:
        return p
    else:
        answer = divide(p)

    return answer


p = "()))((()"
print(solution(p))
