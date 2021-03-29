# 백준 12904 G5
# A와 B

import sys
input = sys.stdin.readline


def isPossible(_s1, _s2):
    while _s2 != _s1:
        tail_char = _s2[-1]
        if tail_char == 'B':
            _s2 = _s2[:-1][::-1]
        else:
            _s2 = _s2[:-1]

        if len(_s2) < len(_s1):
            return False

    return True

s1 = input().rstrip()
s2 = input().rstrip()

if isPossible(s1, s2):
    print(1)
else:
    print(0)