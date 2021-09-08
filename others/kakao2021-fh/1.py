# 카카오 블라인드 2021 1번
# 신규 아이디 추천


# 대문자 -> 소문자
# '소문자숫자-_.' 제외 모두 제거
# . 2개 이상 1개
# . 처음이나 끝 제거
# 빈문자 -> a
# 16자 이상이면 15 제외 모두 제거, .이 마지막이면 제거
# 길이 2이하 -> 마지막 문자를 길이 3 될때까지 반복
import re


def solution(s):
    s = s.lower()
    s = ''.join(re.findall('[a-z0-9-_.]', s))
    s = re.sub('\.+', '.', s)
    s = re.sub('^\.|\.$', '', s)

    if not s:
        s = 'a'
    elif len(s) > 15:
        s = s[:15]
        s = re.sub('\.$', '', s)

    if len(s) == 1:
        s *= 3
    elif len(s) == 2:
        s += s[-1]

    return ''.join(s)


new_id = 'z-+.^....'
print(solution(new_id))
